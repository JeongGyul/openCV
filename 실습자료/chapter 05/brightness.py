import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.add(src, 100)

cv2.imshow('src', src)
cv2.imshow('destination', dst)
cv2.waitKey()
cv2.destroyAllWindows()