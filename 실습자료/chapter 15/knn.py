import cv2
import numpy as np

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

print(digits.shape)   # h: 1000, w: 2000
h, w = digits.shape[:2]

cells = []
for row in np.vsplit(digits, h // 20):
    # row.shape --> (20, 2000)
    # 열 : Column --> col
    # horizontal : 수평의
    for col in np.hsplit(row, w // 20):
        # col.shape --> (20, 20)
        cells.append(col)

cells = np.array(cells)  # list --> ndarray

print(cells.shape)  # (5000, 20, 20)
# 5000 <-- 사진 개수
# 20, 20 <-- 세로, 가로 픽셀 개수

# 2차원의 배열을 1차원의 벡터로 변환
train_images = cells.reshape(5000, 400).astype(np.float32)
train_labels = np.repeat(np.arange(0, 10), len(train_images) / 10)

# Training K-NN
model = cv2.ml.KNearest_create()   # k-nn 객체 생성
model.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

# 마우스로 숫자 적는 기능 구현
oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy  # 로컬 변수 --> 전역 변수
    
    # L <-- Left
    # Botton <-- 버튼
    # Down <-- 아래
    if event == cv2.EVENT_LBUTTONDOWN:    # 마우스 버튼 누르면
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:     # 마우스를 떼면
        oldx, oldy = -1, -1                # 초기화 시켜라

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('Window', img)

# 도화지 준비

img = np.zeros((400, 400), np.uint8)

cv2.imshow('Window', img)
cv2.setMouseCallback('Window', on_mouse)

# 필기체 숫자 인식하기!
while True:
    c = cv2.waitKey()
    if c == 27:    # ESC 키 버튼을 눌렀다면, 종료시켜라
        break

    elif c == 32:     # Space bar의 반환값은 32입니다.
        img_resize = cv2.resize(img, (20, 20), interpolation=(cv2.INTER_AREA))

        img_flatten = img_resize.reshape(-1, 400).astype(np.float32)

        # res <--- 예측한 숫자값
        ret, res, _, _ = model.findNearest(img_flatten, 3)
        print(int(res[0, 0]))   # 예측한 숫자값 출력

        img.fill(0)   # 숫자 인식이 끝났으면, 도화지를 검정색으로 초기화
        cv2.imshow('Window', img)

cv2.destroyAllWindows()