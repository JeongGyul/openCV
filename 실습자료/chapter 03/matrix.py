import cv2

img1 = cv2.imread('dog.bmp')

img2 = img1         # 올바르지 않음
img3 = img1.copy()  # 올바른 복사 방법

img1[:, :] = (0, 255, 255)  # 노란색

cv2.imshow('image #1', img1)
cv2.imshow('image #2', img2)
cv2.imshow('image #3', img3)

cv2.waitKey()
cv2.destroyAllWindows()