import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

stddev = 10
n = np.zeros(src.shape, np.int32)
cv2.randn(n, 0, stddev)

dst = cv2.add(src, n, dtype=cv2.CV_8UC1)

result1 = cv2.GaussianBlur(dst, (0, 0), 5)
result2 = cv2.bilateralFilter(dst, -1, 10, 5)

cv2.imshow('Original', src)
cv2.imshow('+Noise', dst)
cv2.imshow('gaussian', result1)
cv2.imshow('bilateral', result2)
cv2.waitKey()
cv2.destroyAllWindows()