import cv2
# import matplotlib.pyplot as plt
import numpy as np

def calcGrayHist(img):        # Grayscale 영상의 히스토그램 구하는 함수
    channels = [0]
    histSize = [256]   # 빈의 개수
    histRange = [0, 256]   # 256 미만

    h = cv2.calcHist([img], channels, None, histSize, histRange)

    return h

def getGrayHistImage(h):

    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    for x in range(256):
        p1 = (x, 100)       # point의 첫 글자
        p2 = (x, 100 - int((h[x, 0] / np.max(h)) * 100))
        cv2.line(imgHist, p1, p2, 0)     # 검정색 선을 그려라

    return imgHist

def histogram_stretching(src):

    Gmin = float(np.min(src))    # uint8 --> float (실수값)
    Gmax = float(np.max(src))

    dst = ((src - Gmin) / (Gmax - Gmin) * 255.).astype(np.uint8)

    return dst


src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

dst = histogram_stretching(src)

dst2 = cv2.equalizeHist(src)

h = calcGrayHist(src)
h2 = calcGrayHist(dst)
h3 = calcGrayHist(dst2)

cv2.imshow('Org.', src)
cv2.imshow('Org. Hist', getGrayHistImage(h))
cv2.imshow('St', dst)
cv2.imshow('St Hist', getGrayHistImage(h2))
cv2.imshow('Eq', dst2)
cv2.imshow('Eq Hist', getGrayHistImage(h3))
cv2.waitKey()
cv2.destroyAllWindows()


# print(h.shape)   # (256, 1)

# plt.bar(range(256), np.transpose(h)[0])
# plt.grid(True)
# plt.show()