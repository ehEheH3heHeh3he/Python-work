import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
original = cv2.imread('string-lights.webp', cv2.COLOR_BGR2RGB)

# Convert to grayscale
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# define kernel
kernel = np.ones((1, 2), np.uint8)

# Apply thresholding
thresh = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)[1]

# Apply erosion
erosion = cv2.erode(thresh, kernel, iterations=2)

# Apply dilation
dilation = cv2.dilate(erosion, kernel, iterations=4)

# Apply opening
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

# circle the object
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 10:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(original, (x, y), (x+w, y+h), (0, 0 , 0), 3)
        cv2.putText(original, 'Lights', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

# show image
plt.imshow(original, cmap='gray')
plt.show()