import cv2

a = r'E:\code\PreprocessData\data_v7_update\618_photo_class0\9983.jpg'
img = cv2.imread(a,-1)


img = cv2.transpose(img)
img = cv2.flip(img,1)

cv2.imshow('a',img)
cv2.waitKey()