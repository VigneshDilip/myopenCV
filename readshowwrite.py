import cv2
print(cv2.imread('Lenna.png',0))
img=cv2.imread('Lenna.png',-1)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:#Closes when the escape key is pressed
  cv2.destroyAllWindows()
elif k==ord('s'):
  cv2.imwrite('lena1_copy.png',img)
  cv2.destroyAllWindows()
