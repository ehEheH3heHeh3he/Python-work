import numpy as np
import cv2
import datetime
image = cv2.imread('nig.png')
imageLine = image.copy

# pointA = (200,80)
# pointB = (300,80)

# x, y= image.shape[:2]
# y = int(y/2)
# x = int(x/2)
# circle_center = (y,x)

# cv2.circle(image, circle_center, 40, (0,0,255), )
# cv2.arrowedLine(imageLine, pointA, pointB, (0,0,255), 5)

# radius = 40 
# axis1 = (200,80)
# axis2 = (300,80)

# cv2.ellipse(image, axis1, axis1, 0, 0, 360, (0,0,255), 5)
# cv2.ellipse(image, axis1, axis2, 0, 0, 360, (0,0,255), -1)

# point= np.array([[200,80],[300,80],[200,80],[300,80],[20,30],[20,30],[20,30],[20,30],[2,3]])
# cv2.fillConvexPoly(image, point, (0,0,255))


################################



center_x = 150 
center_y = 150  
radius = 50  
color = (0, 255, 0)  
thickness = 2 


for angle in range(0, 360, 45):
    x = int(center_x + radius * np.cos(np.radians(angle)))
    y = int(center_y + radius * np.sin(np.radians(angle)))
    cv2.circle(image, (x, y), radius, color, thickness)


center_radius = 20
cv2.circle(image, (center_x, center_y), center_radius, (0, 0, 255), -1)


###########################################


center_x = 600  
center_y = 200
scale = 100  
color = (0, 0, 255)  
thickness = 2 


cv2.ellipse(image, (center_x - scale // 4, center_y), (scale // 4, scale // 4), 0, 0, 360, color, thickness)
cv2.ellipse(image, (center_x + scale // 4, center_y), (scale // 4, scale // 4), 0, 0, 360, color, thickness)
cv2.ellipse(image, (center_x - scale // 4, center_y), (scale // 4, scale // 4), 0, 0, 180, (0,0,0), thickness)
cv2.ellipse(image, (center_x + scale // 4, center_y), (scale // 4, scale // 4), 0, 0, 180, (0,0,0), thickness)
cv2.line(image, (center_x - scale // 2, center_y), (center_x, center_y + scale // 2), color, thickness)
cv2.line(image, (center_x + scale // 2, center_y), (center_x, center_y + scale // 2), color, thickness)






x = 0  
y = 310  
width = 999
height = 40  
color = (40, 40, 60)  

cv2.rectangle(image, (x, y), (x + width, y + height), color, -1)
              




text = "hello there ?  " + str(datetime.datetime.now()) 
x,y=image.shape[:2]
y=int(y/2-10)
x=int(x/2-150)
org=(x,y)
cv2.putText(image,text,org,fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1.5,color=(255,255,255))

cv2.imshow('nig',image)
cv2.waitKey(0)

cv2.imwrite("nigger.jpg",image)


# napat