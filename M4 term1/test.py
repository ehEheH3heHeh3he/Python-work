import cv2
import numpy as np

img = cv2.imread('OR4EJI0.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([15,50,180])
upper_yellow = np.array([40,255,255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

result = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Masked Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()