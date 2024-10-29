import cv2

# face detection
cap = cv2.VideoCapture(0)

face_cascde = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def create_dataset(img,id,img_id):
    cv2.imwrite("data/pic.%s.%s.png"%(id,img_id),img)

def draw_boundary(img,text) :
    gray_cap = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    face_detect = face_cascde.detectMultiScale(gray_cap)
    xywh = []
    for (x, y, w, h) in face_detect: 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        cv2.putText(img,text,(x-10,y-10), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,255),3)
        xywh = [x,y,w,h]
    return img, xywh

def detect(img,img_id):
    img,xywh = draw_boundary(img,'face')
    id = 1
    if len(xywh) == 4:
        result = img[xywh[1]:xywh[1]+xywh[3],xywh[0]:xywh[0]+xywh[2]]
        create_dataset(result,id,img_id)
    return img

img_id = 1

while True:
    chack,frame = cap.read()
    frame = detect(frame,img_id)
    cv2.imshow("output",frame)
    img_id+=1
    if cv2.waitKey(50) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()