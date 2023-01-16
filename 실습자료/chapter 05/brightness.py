import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

# dst1 = src + 100 # 픽셀값이 255보다 큰 경우 발생. add 쓰는게 좋음
# dst2 = src - 100 # 픽셀값이 0보다 작은 경우 발생. subtract 쓰는게 좋음

dst1 = cv2.add(src, 100)  # 더하기 (밝게)
dst2 = cv2.subtract(src, 100) # 빼기 (어둡게)

cv2.imshow('source', src)
cv2.imshow('add', dst1)
cv2.imshow('subtract', dst2)
cv2.waitKey()
cv2.destroyAllWindows()