import cv2

# B-G-R 색상 모델
src = cv2.imread('pepper.bmp', cv2.IMREAD_COLOR)

rgb_planes = cv2.split(src)
blue_plane = rgb_planes[0]

# YCrCb 색상 모델로 변환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

ycrcb_planes = cv2.split(src_ycrcb)
ycrcb_planes = list(ycrcb_planes)    # tuple -> list로 변환

ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])   # Y 채널 정보

dst_ycrcb = cv2.merge(ycrcb_planes)

dst_rgb = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)
blue_plane2 = cv2.split(dst_rgb)[0]


cv2.imshow('src', src)
cv2.imshow('blue1', blue_plane)
cv2.imshow('blue2', blue_plane2)
cv2.imshow('dst', dst_rgb)
cv2.waitKey()
cv2.destroyAllWindows()