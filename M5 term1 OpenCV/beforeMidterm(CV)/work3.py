import cv2
import datetime
def add_text_to_frame(frame, text):
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (50, 50) 
    font_scale = 1
    color = (255, 0, 0) 
    thickness = 2
    cv2.putText(frame, text, position, font, font_scale, color, thickness)


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    
    if not ret:
        break

    
    text = str(datetime.datetime.now())

    add_text_to_frame(frame, text)

    
    cv2.imshow('Camera', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()