import cv2
print(cv2.imread('Lenna.png',0))
img=cv2.imread('Lenna.png',0)
cv2.imshow('image',img)
cv2.waitKey(15000)
cv2.destroyAllWindows()
