import numpy as np
import cv2, time


number, last = 0, 0
# open video
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # thresh frame
        thresh, result = cv2.threshold(gray_frame, 70, 255, cv2.THRESH_BINARY_INV)
        # apply closing function
        kernel = np.ones((9, 9), np.uint8)
        closing = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel,300)

        contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        value = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 2000:
                x, y, w, h = cv2.boundingRect(contour)

                # draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

                size = cv2.contourArea(contour)

                # insert text
                # if 4000 < size < 6000 :
                #     type = '1 Baht'
                #     value += 1
                # elif 6000 < size < 7500 :
                #     type = '5 Baht'
                #     value += 5
                # elif 7500 < size < 9000 :
                #     type = '10 Baht'
                #     value += 10
                # else :
                type = f'{x},{y}'
                value += 1
                if x == 0 and y == 0:
                    print('table1')
                elif x == 1 and y == 1:
                    print('table2')
                elif x == 2 and y == 2:
                    print('table3')
                
                cv2.putText(frame, type, (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
                # cv2.putText(frame, 'Total : '+str(value), (15,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                frame2 = frame.copy()
                cv2.putText(frame2, 'Total : '+str(value), (15,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            
            if value != last:
                print(value)
                last = value
        cv2.imshow('frame', frame2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break