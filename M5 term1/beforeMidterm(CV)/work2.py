import cv2 

vid = cv2.VideoCapture("vdo_tesst.mov")

while True:
    _, frame = vid.read()
    if _ == True:
        
        hight, width, _ = frame.shape
        print(hight, '-', width)
        frameKiri = frame[0:hight, 0:int(width/2)]
        frameKanan = frame[0:hight, int(width/2):width]

        cv2.imshow('Video', frame)
        cv2.imshow('Video Kiri', frameKiri)
        cv2.imshow('Video Kanan', frameKanan)

        key = cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
    else:
        break