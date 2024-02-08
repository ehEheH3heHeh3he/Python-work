import numpy as np
import cv2
import time
import RPi.GPIO as GPIO

table1, table2, table3, table4, table5 = 16, 7, 19, 13, 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(table1, GPIO.OUT)
GPIO.setup(table2, GPIO.OUT)
GPIO.setup(table3, GPIO.OUT)
GPIO.setup(table4, GPIO.OUT)
GPIO.setup(table5, GPIO.OUT)

# open video
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # thresh frame
        thresh, result = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY_INV)
        # apply closing function
        kernel = np.ones((9, 9), np.uint8)
        closing = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel,150)

        contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        value = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 400:
                x, y, w, h = cv2.boundingRect(contour)

                # draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

                size = cv2.contourArea(contour)

                # insert text
                type =f"{x},{y}"
                value += 1

                current_time = int(time.strftime("%H"))
                if 18 <= current_time or current_time <= 6 :
                    GPIO.output(table1,GPIO.HIGH)
                    GPIO.output(table2,GPIO.HIGH)
                else :
                    GPIO.output(table1,GPIO.LOW)
                    GPIO.output(table2,GPIO.LOW)
                # print("The current time is", current_time)

                cv2.rectangle(frame, (440, 300), (600, 460), (255, 255, 255), 1)
                cv2.rectangle(frame, (440, 150), (600, 290), (255, 255, 255), 1)
                cv2.rectangle(frame, (340, 40) , (590, 120), (255, 255, 255), 1)

                if 440 < x < 600 and 300 < y < 460:
                    GPIO.output(table4,GPIO.HIGH)
                elif 440 < x < 600 and 150 < y < 290:
                    GPIO.output(table3,GPIO.HIGH)
                elif 340 < x < 590 and 40 < y < 120:
                    GPIO.output(table5,GPIO.HIGH)
                else:
                    GPIO.output(table3,GPIO.LOW)
                    GPIO.output(table4,GPIO.LOW)
                    GPIO.output(table5,GPIO.LOW)
                


                
                
                cv2.putText(frame, type, (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
                # cv2.putText(frame, 'Total : '+str(value), (15,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                frame2 = frame.copy()
                cv2.putText(frame2, 'Total : '+str(value), (15,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        
        frame2 = frame.copy()
        cv2.imshow('frame', frame2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            GPIO.cleanup()
            break
    else:
        break

GPIO.cleanup()

