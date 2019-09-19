import cv2
img = cv2.imread('watch.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(500)
cv2.destroyAllWindows()