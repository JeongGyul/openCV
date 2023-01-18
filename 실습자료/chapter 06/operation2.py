import cv2

src1 = cv2.imread('diff1.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('diff2.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src1, src2)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

cv2.imshow('Add', src1)
cv2.imshow('AddWeighted', src2)
cv2.imshow('Subtract', dst3)
cv2.imshow('Abs. Diff.', dst4)

cv2.waitKey()
cv2.destroyAllWindows()
# cv2.destroyWindow('AddWeighted')