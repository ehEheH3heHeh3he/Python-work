import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Load image
# img = cv2.imread('coin3.png', 0)

# # Apply adaptive thresholding
# original = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 4)

# # Define kernel
# kernel = np.ones((2, 2), np.uint8)

# # Apply erosion
# erosion =cv2.erode(original, kernel, iterations=1)

# # Apply dilation
# dilation = cv2.dilate(original, kernel, iterations=1)

# # Apply opening
# opening = cv2.morphologyEx(original, cv2.MORPH_OPEN, kernel)

# #Apply closing
# closing = cv2.morphologyEx(original, cv2.MORPH_CLOSE, kernel)

# # Apply gradient
# gradient = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel)

# # Show image
# titles = ['Original', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
# for i in range(6):
#     plt.subplot(2, 3, i+1, title=titles[i], xticks=[], yticks=[]), plt.imshow(eval(titles[i].lower()), cmap='gray')
# plt.show()

#----------------------------------------------
# lab1
# Load image
# img = cv2.imread('coin3.png', 0)

# # crop out something in image
# img = img[1123:1427, 1641:1947]

# # define kernel
# kernel1 = np.ones((3, 3), np.float32)/9 # 3x3 kernel

# print(img)
# # Apply filter2D
# filter2d = cv2.filter2D(img, -1, kernel1)

# # Apply mean filter
# mean = cv2.blur(img, (5, 5))

# # Apply median filter
# median = cv2.medianBlur(img, 5)

# # Apply Gaussian filter
# gaussian = cv2.GaussianBlur(img, (5, 5), 10)


# # Show image
# title = ['Img', 'Filter2D', 'Mean', 'Median', 'Gaussian']
# for i in range(5):
#     plt.subplot(2, 3, i+1, title=title[i], xticks=[], yticks=[]), plt.imshow(eval(title[i].lower()), cmap='gray')
# plt.show()

#----------------------------------------------
# problem1
# Load image
original = cv2.imread('coin3.png')
img = cv2.imread('coin3.png', 0)

# Define kernel
kernel = np.ones((2, 2), np.uint8)

# crop image
grayscale = img[1123:1427, 1641:1947]

# Apply mean filter
mean = cv2.blur(grayscale, (5, 5))

# Apply adaptive thresholding
tresh = cv2.adaptiveThreshold(mean, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 4)

# Apply opening
result = cv2.morphologyEx(tresh, cv2.MORPH_OPEN, kernel) # opening is used because there's a lot of noise in the background

# Show image
titles = ['Original','Grayscale', 'Mean', 'Tresh', 'Result']
for i in range(len(titles)):
    plt.subplot(2, 3, i+1, title=titles[i], xticks=[], yticks=[]), plt.imshow(eval(titles[i].lower()), cmap='gray')
plt.show()