import cv2
import numpy as np
image=cv2.imread('img.jpg')
image_gray=cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
image_gray=cv2.GaussianBlur (image_gray, (5,5),0)
_, im_th=cv2.threshold(image_gray,155,255,cv2.THRESH_BINARY_INV)
_, ctrs, _=cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rects=[cv2.boundingRect(ctr) for ctr in ctrs]

for rect in rects:
    cv2.rectangle(image, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]),
(0,0,255),3)
cv2.imshow('image', image)
cv2.imshow('image_gray', image_gray)
cv2.imshow('image_threshold',im_th)
cv2.waitKey(0)
cv2.destroyAllWindows()