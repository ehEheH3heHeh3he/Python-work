import numpy as np
import cv2

image = cv2.imread('download.png')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([155,25,0])
upper = np.array([179,255,255])
mask = cv2.inRange(image, lower, upper)
blurred = cv2.GaussianBlur(mask,(5,5),0)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('mask',image)
cv2.waitKey()