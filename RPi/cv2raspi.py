import numpy as np
import cv2 as cv2

COLOR_ROW = 80
COLOR_COLS = 250
capture = cv2.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)

if not capture.isOpened():
    raise RuntimeError('Error opening')

colorAray = np.zeros((COLOR_ROW,COLOR_COLS,3),dtype=np.uint8)

while True:
    (grabbed,frame) = capture.read()
    height,width = frame.shape[:2]

    cv2.circle(frame,(int(width/2),int(height/2)),20,(0,0,255),0)
    cv2.imshow('Video',frame)

    if not grabbed:
        break

    keyVal = cv2.waitKey(1) & 0xFF
    if keyVal == ord('q'):
        break

    snapshot = frame.copy()

    colorAray[:] = snapshot[int(height/2),int(width/2),:]
    rgb = snapshot[int(height/2),int(width/2),[2,1,0]]


    luminance = 1-(0.299*rgb[0]+0.587*rgb[1]+0.114*rgb[2]) / 255
    if luminance < 0.5:
        textColor =[0,0,0]
    else:
        textColor =[0,0,0]

        cv2.putText(colorAray,str(rgb),(20, COLOR_ROW - 20),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.8,color = textColor)
        cv2.imshow('Color',colorAray)


capture.release()
cv2.destroyAllWindows()