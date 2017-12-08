# -*- coding:utf-8 -*- 

import cv2
import dlib
import numpy as np 
    

cap = cv2.VideoCapture(0)
cap.isOpened()

def ket_points(img):
    # 人脸关键点检测
    PREDICTOR_PATH = "../../some-big-model-file/shape_predictor_68_face_landmarks.dat"
    
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    rects = detector(img,1)
    points_keys = []

    for i in range(len(rects)):
        landmarks = np.matrix([[p.x,p.y] for p in predictor(img,rects[i]).parts()])
        img = img.copy()
        for idx,point in enumerate(landmarks):
            pos = (point[0,0],point[0,1])
            points_keys.append(pos)
            cv2.circle(img,pos,2,(255,0,0),-1)
    return img

def frontalface(img):
    # 人脸检测
    face_cascade = cv2.CascadeClassifier(r'/opt/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(
        gray,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5))

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)
        # cv2.circle(img,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
    return img


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_key = ket_points(gray)
    face_detector = frontalface(gray)
    cv2.imshow('frame',face_key)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


