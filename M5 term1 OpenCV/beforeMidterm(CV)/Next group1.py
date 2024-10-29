import cv2
import numpy as np

img = cv2.imread('OR4EJI0.jpg')
x,y = img.shape[:2]
x2 = int(x/2)
y2 = int(y/2)
if x2 > y2:
    z = x2
else:
    z = y2
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([15,50,180])
upper_yellow = np.array([40,255,255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

result = cv2.bitwise_and(img,img, mask= mask)

circle = np.zeros((x, y,3), dtype="uint8")

cv2.circle(circle, (x2, y2), z,(255,255, 255), -1)
bitwiseAnd = cv2.bitwise_and(result, circle)

cv2.imshow('Mask',bitwiseAnd)
cv2.waitKey(0)
# cv2.imshow('Masked Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows() 