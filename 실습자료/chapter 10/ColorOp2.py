import cv2

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

# split : v. 쪼개다
bgr_planes = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('Blue', bgr_planes[0])
cv2.imshow('Green', bgr_planes[1])
cv2.imshow('Red', bgr_planes[2])

cv2.waitKey()
cv2.destroyAllWindows()