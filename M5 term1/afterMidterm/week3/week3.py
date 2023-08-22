import cv2 as cv

vid = cv.VideoCapture(0)
ret, frame1 = vid.read()
ret, frame2 = vid.read()

while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:  

        motiondiff = cv.absdiff(frame1,frame2)

        grayimg = cv.cvtColor(motiondiff,cv.COLOR_BGR2GRAY)

        blur = cv.GaussianBlur(grayimg,(5,5),0)

        thresh, result = cv.threshold(blur,50,255,cv.THRESH_BINARY)

        dilation = cv.dilate(result,None,iterations=3)

        contours,hierarchy = cv.findContours(dilation,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

        draw_contour = cv.drawContours(frame1,contours,-1,(0,255,255),2)

    for contour in contours:

        (x,y,w,h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 1800:
            continue        
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,0,120),5)

    cv.imshow("Frame",frame1)

    frame1 = frame2
    ret, frame2 = vid.read()
    key = cv.waitKey(30)
    if key == ord("q"):
        break

vid.release()
cv.destroyAllWindows()