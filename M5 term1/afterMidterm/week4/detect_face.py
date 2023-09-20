import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img_id=0
id = 1
def draw_boundary(img,clf):
      gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      face_detect=face_cascade.detectMultiScale(gray_img,1.1,5) 
      xywh = []
      for (x,y,w,h) in face_detect :
            cv2.rectangle(img, (x,y), (x+w, y+ h), (0,255,0),5) 
            cv2.rectangle(img,(x,y-50),(x+w,y),(0,0,255), -1)
            id, con = clf.predict(gray_img[y:y+h,x:x+w])
            if con <= 65 and id == 1:
                     cv2.putText(img, "Next", (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3) 
              
            elif con <= 65 and id == 2:
                     cv2.putText(img, "Artie", (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
              
            elif con <= 65 and id == 3:
                     cv2.putText(img, "Neem", (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
              
            elif con <= 65 and id == 4:
                     cv2.putText(img, "Mint", (x+10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

            else: 
                     cv2.putText(img, "unknow", (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
            show_con ="{0}%".format(round(100-con))
            cv2.rectangle(img, (x+10,y+h+10), (x+w,y+h+50), (255,0,255), -1)
            cv2.putText(img, show_con, (x+10,y+h+40), cv2.FONT_HERSHEY_SIMPLEX,0.8, (255,255,255), 2) 
            xywh=[x,y,w,h]
            
      return img,xywh

def detect(img,img_id,clf) :
      img,xywh=draw_boundary(img, clf) 
      if len(xywh) == 4 :
            result=img[xywh[1]:xywh[1 ]+xywh[3],xywh[0]:xywh[0]+xywh[2]]
      return img

clf=cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

while (True):
      check, frame=cap.read()
      frame=detect(frame,img_id,clf)
      cv2.imshow("output camera",frame)
      img_id +=1
      if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destoryAllWindows()