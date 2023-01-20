import cv2

cap = cv2.VideoCapture('vtest.avi')

hog = cv2.HOGDescriptor()  # 클래스 호출을 통해 객체 생성

# set <-- 설정하다
# SVM <-- 머신러닝 기술 이름
# Detector <-- 검출자
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 프레임(Frame)은 동영상을 구성하는 한 장, 한 장의 사진을 뜻함
while True:
    ret, frame = cap.read()    # 프레임(Frame)을 읽어서 반환하라
    # ret <-- True / False
    # True : 동영상 Frame을 정상적으로 읽었을 때,
    # False : 동영상 Frame이 비정상적으로 읽혔을 때
    if not ret:
        break   # Frame이 비정상적으로 읽혔을 때, 루프 탈출

    detected, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detected:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow('CCTV', frame)

    if cv2.waitKey(10) == 27:    # 10 <-- ASCII (ESC키를 의미)
        # cv2.waitKey('ESC') --> 27 반환하게 되어있음
        break

cv2.destroyAllWindows()