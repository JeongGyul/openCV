import cv2

print(cv2.__version__)

img = cv2.imread('lenna.bmp')   # image + read

cv2.namedWindow('image')   # 이름 붙어진 창
cv2.imshow('image', img)       # image + show
cv2.waitKey()   # 사용자로부터 키보드 입력을 기다립니다.
# cv2.destroyAllWindows()
cv2.destroyWindow('image')