import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

#ndarray <--------- n-dimensional array (n 차원의 배열)
print(type(img))   # img 변수에 저장된 데이터의 타입(자료형)
print(img.shape)   # img 변수가 어떤 구조인지 확인

cv2.namedWindow('cat')
cv2.imshow('cat', img)
cv2.waitKey()
cv2.destroyAllWindows()