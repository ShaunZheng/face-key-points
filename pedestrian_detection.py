# -*- coding:utf-8 -*-
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np 
import argparse
import imutils
import cv2
import os
from skimage import io


def detector(img):
    # 初始化HOG描述符/人检测器
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # image = cv2.imread(img)
    image = io.imread(img)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()

    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
        padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # show the output images
    # cv2.imshow("Before NMS", orig)
    # cv2.imshow("After NMS", image)
    # cv2.waitKey(0)
    return image



cap = cv2.VideoCapture(0)
cap.isOpened()

# cap = cv2.VideoCapture("../video_images/people2.mp4")


while(True):
    ret, frame = cap.read()
    # # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # rows,cols = frame.shape[:2]
    # #第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
    # M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1.5)
    # #第三个参数：变换后的图像大小
    # res = cv2.warpAffine(frame,M,(rows,cols))

    # detect = detector(res)
    cv2.imshow('ok',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



