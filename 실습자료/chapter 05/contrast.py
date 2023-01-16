import cv2
import numpy as np    # 넘파이(numpy)

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# s = 2.0
# dst = cv2.multiply(src, s)    # 모든 픽셀 값에 s만큼 곱하기

alpha = 1.0
# (수식) dst(x, y) = src(x, y) + (src(x, y) - 128) * alpha
dst = np.clip(src + (src - 128.) * alpha, 0, 255).astype(np.uint8)
# uint <-- unsigned integer

cv2.imshow('source', src)
cv2.imshow('destination', dst)
cv2.waitKey()
cv2.destroyAllWindows()