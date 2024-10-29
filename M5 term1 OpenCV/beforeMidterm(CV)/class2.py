import cv2

img = cv2.imread('download.png')
# vdo = cv2.VideoCapture("vdo_tesst.mov")
# vid = cv2.VideoCapture(0)
# while(vid.isOpened()):
#     ret, frame = vid.read()
#     if ret == True:
#         cv2.imshow('Frame', frame)
#         if cv2.waitKey(380) & 0xFF == ord('q'):
#             break
#     else:
#         break

# frame_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
# frame_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
# frame_size = (int(frame_width), int(frame_height))
# fps = 30

# vidsave = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, frame_size)
# while(vid.isOpened()):
#     ret, frame = vid.read()
#     if ret == True:
#         vidsave.write(frame)
#         cv2.imshow('Frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cv2.imshow('original', image)

down_width = 200
down_height = 200
down_point = (down_width, down_height)
resized_down = cv2.resize(img,down_point,interpolation=cv2.INTER_LINEAR)

up_width = 400
up_height = 400
up_point = (up_width, up_height)
resized_up = cv2.resize(img,up_point,interpolation=cv2.INTER_LINEAR)

scale_up = 2
scale_down = 0.5
scaled_f_down = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(img, None, fx=scale_up, fy=scale_up, interpolation=cv2.INTER_LINEAR)


# cropped = img[0:200, 0:200]
cropped = img[startrow:endrow, startcol:endcol]

cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.imshow('Resized Up by defining height and width', resized_up)
cv2.imshow('Resized Down by defining scale factor', scaled_f_down)
cv2.imshow('Resized Up by defining scale factor', scaled_f_up)
cv2.waitKey(0)
cv2.destroyAllWindows()