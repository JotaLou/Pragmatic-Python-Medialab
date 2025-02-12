import cv2 
import numpy as np
import urllib.request, io


urldata = urllib.request.urlopen('https://i.pinimg.com/564x/fd/8b/6c/fd8b6c1cead77cc8929380611e90237c.jpg')
data_stream = np.asarray(bytearray(urldata.read()), dtype=np.uint8)
img = cv2.imdecode(data_stream, -1)

"""#Original image
cv2.imshow('img', img)
cv2.waitKey(0)
"""
#Convert to greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Detect Edges (Canny algorithm)
edges = cv2.Canny(gray, 40, 55, apertureSize= 3)
edges = cv2.bitwise_not(edges)  #Invert colors

# Edges on the hand
cv2.imshow("edges in palm", edges)
cv2.waitKey(0)


cv2.imwrite("palmlines.jpg", edges)
palmlines = cv2.imread("palmlines.jpg")
img2 = cv2.addWeighted(palmlines, 0.3, img, 0.7, 0)

cv2.imshow("Detected edges",img2)
cv2.waitKey(0)