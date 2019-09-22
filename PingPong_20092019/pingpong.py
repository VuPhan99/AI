import cv2 
import numpy as np 
import imutils

cap = cv2.VideoCapture('D:\XuanVu\AI\PingPong_20092019\pingpong.mp4')

while(True):
    ret,frame=cap.read()
    blur=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    cv2.line(frame, (410, 0), (460, 520),(0,0,255), 2)
    cv2.putText(frame, "Score: 1 / 1",(20, 30),cv2.FONT_HERSHEY_COMPLEX,.7,(0,0,255),)

    lower=np.array([5,100,20])
    upper = np.array([25,255,255])
    mask= cv2.inRange(hsv,lower,upper)
    mask = cv2.erode(mask,None,iterations=2)
    mask= cv2.dilate(mask,None, iterations =2)

    ball_center = None
    ball_cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    ball_cnts = imutils.grab_contours(ball_cnts)
    
    if len(ball_cnts) > 0:
	    c = max(ball_cnts, key=cv2.contourArea)
	    ((x, y), radius) = cv2.minEnclosingCircle(c)
	    M = cv2.moments(c)
	    ball_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	    if radius > 10:
		    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
		    cv2.circle(frame, ball_center, 5, (0, 0, 255), -1)
            
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
