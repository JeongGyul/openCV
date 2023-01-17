import cv2

def calcHist(img):        # 히스토그램을 만들어주는 사용자 정의 함수


src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)