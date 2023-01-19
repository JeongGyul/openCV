import cv2
import numpy as np

src = cv2.imread('butterfly.jpg', cv2.IMREAD_COLOR)

# print(src.shape)    # 배열의 모양 (356, 493, 3)
# print(src.dtype)    # 자료형
#
# print('Blue Image (0, 0)', src[0, 0, 0])
# print('Green Image (0, 0)', src[0, 0, 1])
# print('Red Image (0, 0)', src[0, 0, 2])

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# dst = np.zeros(src.shape, src.dtype)
#
# for j in range(0, src.shape[0]):     # (0, 356)
#     for k in range(0, src.shape[1]):     # (0, 493)
#         p1 = src[j, k, :]
#         p2 = dst[j, k, :]
#
#         p2[0] = 255 - p1[0]    # blue
#         p2[1] = 255 - p1[1]    # green
#         p2[2] = 255 - p1[2]    # red

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()