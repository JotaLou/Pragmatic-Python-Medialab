#from __future__ import print_function
import cv2 as cv
#import argparse

def offset(x_y, target="xy",offset=(0,0)):
    """Offset a 2D tuple by 'offset' units."""
    x, y = x_y
    if target == "x":
        x += offset
        return (x,y)
    elif target == "y":
        y += offset
        return (x,y)
    elif target =="xy" or target == "x_y":
        x += offset[0]
        y += offset[1]
        return (x,y)
    else: 
        raise Exception("Input should be 'x', 'y' or 'xy'")

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    
    #-- Detect Faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x+w//2, y+h//2)
        #Crosshair
        cv.line(frame, offset(center,'y',2), offset(center,'y',6), (255, 255, 255), 1)
        cv.line(frame, offset(center,'y',-2), offset(center,'y',-6), (255, 255, 255), 1)
        cv.line(frame, offset(center,'x',6), offset(center,'x',2), (255, 255, 255), 1)
        cv.line(frame, offset(center,'x',-6), offset(center,'x',-2), (255, 255, 255), 1)
        cv.line(frame, center, center, (255,255,255), 1)
        #Ellipse
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (51, 255, 51), 2)
        
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x+ x2+ w2//2,y+ y2+ h2//2)
            radius = int(round((w2+ h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (20, 20, 20), 2)
    
    cv.imshow("Capture - Face detection", frame)
    
"""
parser = argparse.ArgumentParser(description="Code for Cascade Classifier tutorial.")
parser.add_argument("--face_cascade", help="Path to face cascade.", default="E:\Anaconda3\Lib\site-packages\cv2\data/haarcascades/haarcascade_frontalface_default.xml")
parser.add_argument("--eyes_cascade", help="Path to eyes cascade.", default="E:\Anaconda3\Lib\site-packages\cv2\data/haarcascades/haarcascade_eye.xml")
parser.add_argument("--camera", help="Camera divide number.", type=int, default=0)
args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
"""

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.data.haarcascades + 'haarcascade_frontalface_default.xml'):
    print("--(!)Error loading face cascade")
    exit(0)
if not eyes_cascade.load(cv.data.haarcascades + 'haarcascade_eye.xml'):
    print("--(!)Error loading eyes cascade")
    exit(0)
    
#camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print("--(!)Error opening video capture")
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- break')
        break
    
    detectAndDisplay(frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()