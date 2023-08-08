import cv2 as cv

cap  = cv.VideoCapture(0)

face_cascde = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
scale = 1.1
minNeighbor = 3
# global x,y,w,h
while (cap.isOpened()):
      chack,frame = cap.read()
        #   result = cv.VideoWriter('video/filename.avi',cv.VideoWriter_fourcc(*'MJPG'),30, frame_size)
      if chack :
            gray_cap = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
            face_detect = face_cascde.detectMultiScale(gray_cap)
            for (x, y, w, h) in face_detect: 
                  cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
                  
                  frame_size = (w, h)

                  crop_img = frame[y:y+h, x:x+w]
                  cv.imshow("crop",crop_img)
                  crop_img2 = frame[y:y+h, x:x+w]
                  cv.imshow("crop2",crop_img2)

            cv.imshow("face detect",frame)

            

            if cv.waitKey(1) & 0xFF == ord("q"):
                  break
            if cv.waitKey(1) & 0xFF == ord("p"):
                  cv.imwrite('crop_img.jpg', crop_img)
                  cv.imwrite('crop_img2.jpg', crop_img2)
                  break
      else :
            break

cap.release()
cv.destroyAllWindows()