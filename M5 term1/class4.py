import numpy as np
import cv2

image = cv2.imread('image.png')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0,50,50])
upper = np.array([10,255,255])
mask = cv2.inRange(image, lower, upper)
blurred = cv2.GaussianBlur(mask,(5,5),0)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('mask',mask)
cv2.waitKey()
