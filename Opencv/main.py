import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# def f(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# if __name__ == '__main__':
#     f('PyCharm')

def contour():
    img = cv2.imread('image/test.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    x, contours = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, x, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("image/test2.jpg")
cv2.imshow("img", img)

img_copy = img
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("img_gray", img_gray)
img_blur = cv2.medianBlur(img_gray, 5)
# cv2.imshow("img_blur", img_blur)
img_edge = cv2.adaptiveThreshold(img_blur,
                                 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=7,
                                 C=3)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
# cv2.imshow("img_edge", img_edge)

for _ in range(2):
    img_copy = cv2.pyrDown(img_copy)
    for _ in range(5):
        img_copy = cv2.bilateralFilter(img_copy, d=9, sigmaColor=9, sigmaSpace=7)
    img_copy = cv2.resize(img_copy, (img.shape[1], img.shape[0]),
                          interpolation=cv2.INTER_CUBIC)

img_cartoon = cv2.bitwise_and(img_copy, img_edge)

cv2.imshow("img_copy", img_copy)
cv2.imshow("img_cartoon", img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()