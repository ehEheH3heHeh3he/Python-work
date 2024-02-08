import cv2 as cv

img = cv.imread('download.png',1)
image_copy = img.copy() 
imgheight=img.shape[0]
imgwidth=img.shape[1]
print("Original Height and Width:", imgheight,"x", imgwidth)

cv.imshow('Original Image', img)

cropped_image = img[316:797, 384:896] 
# cv.imshow("cropped", cropped_image)

M = 26
N = 23
x1 = 0
y1 = 0
 
for y in range(0, imgheight, M):
    for x in range(0, imgwidth, N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break  
        y1 = y + M
        x1 = x + N
 
        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1
            tiles = image_copy[y:y+M, x:x+N]
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= imgheight: 
            y1 = imgheight - 1
            tiles = image_copy[y:y+M, x:x+N]
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= imgwidth: 
            x1 = imgwidth - 1
            tiles = image_copy[y:y+M, x:x+N]
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            tiles = image_copy[y:y+M, x:x+N]
            cv.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)

cv.imshow("Patched Image",img)

cv.waitKey(0)
cv.destroyAllWindows()