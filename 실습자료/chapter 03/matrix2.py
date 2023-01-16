import cv2

img1 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)

img2 = img1[200:400, 200:400, :] # 공유
img3 = img1[200:400, 200:400, :].copy() # 복사

img2 += 50       # 모든 픽셀값을 50만큼 증가

cv2.imshow('girl', img1)
cv2.imshow('#1', img2)
cv2.imshow('#2', img3)
cv2.waitKey()
cv2.destroyAllWindows()