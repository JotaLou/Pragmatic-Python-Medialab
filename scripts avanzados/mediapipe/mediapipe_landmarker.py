import time
import cv2 as cv   #openCV
import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

class landmarker_and_result():
   def __init__(self):
      self.result = mp.tasks.vision.HandLandmarkerResult
      self.landmarker = mp.tasks.vision.HandLandmarker
      self.createLandmarker()
   
   def createLandmarker(self):
      # callback function
      def update_result(result, output_image: mp.Image, timestamp_ms: int):
         self.result = result

      # HandLandmarkerOptions (details here: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python#live-stream)
      options = mp.tasks.vision.HandLandmarkerOptions( 
         base_options = mp.tasks.BaseOptions(model_asset_path="hand_landmarker.task"), # path to model
                                             #delegate=mp.tasks.BaseOptions.Delegate.GPU), 
         running_mode = mp.tasks.vision.RunningMode.LIVE_STREAM, # running on a live stream
         num_hands = 2, # track both hands
         min_hand_detection_confidence = 0.4, # lower than value to get predictions more often
         min_hand_presence_confidence = 0.4, # lower than value to get predictions more often
         min_tracking_confidence = 0.4, # lower than value to get predictions more often
         result_callback=update_result)
      
      # initialize landmarker
      self.landmarker = self.landmarker.create_from_options(options)
   
   def detect_async(self, frame):
      # convert np frame to mp image
      mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
      # detect landmarks
      self.landmarker.detect_async(image = mp_image, timestamp_ms = int(time.time() * 1000))

   def close(self):
      # close landmarker
      self.landmarker.close()


def draw_landmarks_on_image(rgb_image, detection_result):
   """Courtesy of https://github.com/googlesamples/mediapipe/blob/main/examples/hand_landmarker/python/hand_landmarker.ipynb"""
   try:
      if detection_result.hand_landmarks == []:
         return rgb_image
      else:
         hand_landmarks_list = detection_result.hand_landmarks
         annotated_image = np.copy(rgb_image)

         # Loop through the detected hands to visualize.
         for idx in range(len(hand_landmarks_list)):
            hand_landmarks = hand_landmarks_list[idx]
            
            # Draw the hand landmarks.
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
               landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks])
            mp.solutions.drawing_utils.draw_landmarks(
               annotated_image,
               hand_landmarks_proto,
               mp.solutions.hands.HAND_CONNECTIONS,
               mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
               mp.solutions.drawing_styles.get_default_hand_connections_style())
         return annotated_image
   except:
      return rgb_image


def count_fingers_raised(rgb_image, detection_result):
   """Iterate through each hand, checking if fingers (and thumb) are raised. Hand landmark enumeration 
       comes from: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker."""
   try:
      # Get Data
      hand_landmarks_list = detection_result.hand_landmarks

      # Code to count numbers of fingers raised will go here
      numRaised = 0
      # for each hand...
      for idx in range(len(hand_landmarks_list)):
         # hand landmarks is a list of landmarks where each entry in the list has an x, y, and z in normalized image coordinates
         hand_landmarks = hand_landmarks_list[idx]
         # for each fingertip... (hand_landmarks 4, 8, 12, and 16)
         for i in range(8,21,4):
            # make sure finger is higher in image the 3 proceeding values (2 finger segments and knuckle)
            tip_y = hand_landmarks[i].y
            dip_y = hand_landmarks[i-1].y
            pip_y = hand_landmarks[i-2].y
            mcp_y = hand_landmarks[i-3].y
            if tip_y < min(dip_y,pip_y,mcp_y):
               numRaised += 1
         # for the thumb
         # use direction vector from wrist to base of thumb to determine "raised"
         tip_x = hand_landmarks[4].x
         dip_x = hand_landmarks[3].x
         pip_x = hand_landmarks[2].x
         mcp_x = hand_landmarks[1].x
         palm_x = hand_landmarks[0].x
         if mcp_x > palm_x:
            if tip_x > max(dip_x,pip_x,mcp_x):
               numRaised += 1
         else:
            if tip_x < min(dip_x,pip_x,mcp_x):
               numRaised += 1

      # Code to display the number of fingers raised will go here
      annotated_image = np.copy(rgb_image)
      height, width, _ = annotated_image.shape
      text_x = int(hand_landmarks[0].x * width) - 100
      text_y = int(hand_landmarks[0].y * height) + 50
      cv.putText(img = annotated_image, text = str(numRaised) + " Fingers Raised",
          org = (text_x, text_y), fontFace = cv.FONT_HERSHEY_DUPLEX,
          fontScale = 1, color = (0,0,255), thickness = 2, lineType = cv.LINE_4)
      return annotated_image
   except:
      return rgb_image

def main():
    # Acedemos a la cámara
    capture = cv.VideoCapture(0)
    # creamos el objeto landmarker
    hand_landmarker = landmarker_and_result()

    while True:
        ret, frame = capture.read() # Leemos el frame
        frame = cv.flip(frame,1)    # Espejo a la imagen
        frame = draw_landmarks_on_image(frame, hand_landmarker.result)
        frame = count_fingers_raised(frame, hand_landmarker.result)
        cv.imshow('frame', frame)   # Mostramos en pantalla   
        hand_landmarker.detect_async(frame)
        #print(hand_landmarker.result)
        if cv.waitKey(1) == ord('q'): # Si pulsamos "q" se sale del programa
            break 

    # Liberamos los recursos
    capture.release()
    cv.destroyAllWindows()
    hand_landmarker.close()


if __name__ == "__main__":
    main()