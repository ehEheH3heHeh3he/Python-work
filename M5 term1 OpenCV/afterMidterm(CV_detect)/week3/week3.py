import cv2

# get vedio from webcam
vid = cv2.VideoCapture(0)
ret, frame1 = vid.read()
ret, frame2 = vid.read()

while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:  
        # compare two frames
        motiondiff = cv2.absdiff(frame1,frame2)
        # convert to gray scale
        grayimg = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        # blur the image
        blur = cv2.GaussianBlur(grayimg,(5,5),0)
        # threshold
        thresh, result = cv2.threshold(blur,50,255,cv2.THRESH_BINARY)
        # dilate the image
        dilation = cv2.dilate(result,None,iterations=3)
        # find contours
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # draw contours
        draw_contour = cv2.drawContours(frame1,contours,-1,(0,255,255),2)
    # show the result
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        # ignore small contours
        if cv2.contourArea(contour) < 1800:
            continue        
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,120),5)

    cv2.imshow("Frame",frame1)
    # update frames
    frame1 = frame2
    ret, frame2 = vid.read()
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()