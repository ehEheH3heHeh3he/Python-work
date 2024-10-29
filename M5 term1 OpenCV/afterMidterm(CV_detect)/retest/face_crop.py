import cv2 as cv

cap  = cv.VideoCapture(0)

face_cascde = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
scale = 1.1
minNeighbor = 3
detected_face_positions = []
# global x,y,w,h
while (cap.isOpened()):
      chack,frame = cap.read()
        #   result = cv.VideoWriter('video/filename.avi',cv.VideoWriter_fourcc(*'MJPG'),30, frame_size)
      detected_face_positions.clear()
      if chack :
            gray_cap = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
            face_detect = face_cascde.detectMultiScale(gray_cap)
            
            for (x, y, w, h) in face_detect: 
                  cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
                  frame_size = (w, h)
                  detected_face_positions.append((x, y, w, h))
                  print(detected_face_positions)
                  crop_img = frame[int(detected_face_positions[len(face_detect)-1][1]):int(detected_face_positions[len(face_detect)-1][1])+int(detected_face_positions[len(face_detect)-1][3]), int(detected_face_positions[len(face_detect)-1][0]):int(detected_face_positions[len(face_detect)-1][0])+int(detected_face_positions[len(face_detect)-1][2])]
                  cv.imshow("crop",crop_img)
          
                  # crop_img2 = frame[int(detected_face_positions[1][1]):int(detected_face_positions[1][1])+int(detected_face_positions[1][3]), int(detected_face_positions[1][0]):int(detected_face_positions[1][0])+int(detected_face_positions[1][2])]
                  # cv.imshow("crop2",crop_img2)
                  
            cv.imshow("face detect",frame)

            # not done yet

            if cv.waitKey(1) & 0xFF == ord("q"):
                  break
            if cv.waitKey(1) & 0xFF == ord("p"):
                  cv.imwrite('crop_img.jpg', crop_img)
                  # cv.imwrite('crop_img2.jpg', crop_img2)
                  break
      else :
            break

cap.release()
cv.destroyAllWindows()