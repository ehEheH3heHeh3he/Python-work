import cv2
import matplotlib.pyplot as plt
import numpy as np

# x =[1,3,4,8]
# y =[2,4,6,8]
# x2 = [1,2,3,4]
# y2 = [2,4,6,8]
# plt.plot(x,y, label='First Line')
# plt.plot(x2,y2, label='Second Line')
# plt.xlabel('Plot Number')
# plt.ylabel('Important var')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()


# plt.subplot(1,2,1, title='Original', xticks=[], yticks=[])
# plt.imshow(img)
# plt.subplot(1,2,2, title='fixed', xticks=[], yticks=[])
# plt.imshow(img[:,:,::-1])
# plt.show()

# img = cv2.imread('MicrosoftTeams-image.png',0)
# imH = img.shape[0]
# imW = img.shape[1]
# binary = np.zeros((imH,imW), dtype=np.uint8)
# for i in range(imH):
#     for j in range(imW):
#         if img[i,j] > 80:
#             binary[i,j] = 255
#         else:
#             binary[i,j] = 
# plt.imshow(binary, cmap='gray')
# plt.show()

# img = cv2.imread('MicrosoftTeams-image.png',0)   
# thresh_value = [70,90,110,150,200]
# plt.subplot(231,title='Original', xticks=[], yticks=[])
# plt.imshow(img, cmap='gray')
# for i in range(len(thresh_value)):
#     thresh,result = cv2.threshold(img, thresh_value[i], 255, cv2.THRESH_BINARY)
#     plt.subplot(232+i,title='Thresh Value %d'%(thresh_value[i]), xticks=[], yticks=[])
#     plt.imshow(result, cmap='gray')
#     plt.title('Thresh Value')
# plt.show()

img = cv2.imread('coinnn.png',0)   
plt.subplot(121,title='Original', xticks=[], yticks=[])
plt.title('Original')
plt.imshow(img, cmap='gray')

result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,9,5) #ใช้เกาส์เซียนเพื่อลด noise ในภาพ และใช้ไบนารี่เพื่อทำให้ภาพเป็นขาวดำก่อน กลุ่ม : เน็กซ์เทพซ่าไปล่าหมา
plt.subplot(122,title='Adaptive Threshold Gaussian', xticks=[], yticks=[])
plt.title('Adaptive Threshold Gaussian')
plt.imshow(result, cmap='gray') 
plt.show()