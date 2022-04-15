import cv2
import os

fire_cascade=cv2.CascadeClassifier('fire_detection.xml')
cam = cv2.VideoCapture(0)
c=0
while(True):
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame,1.2,5)
    for(x,y,w,h) in fire:
        roi_gray=gray[y:y+h , x:x+w]
        roi_color=frame[y:y+h , x:x+w]
        print('Fire is detected')
        if(c==0):
            c=c+1
            file = "fire.mp3"
            os.system("start " + file)
    cv2.imshow('Camera Detector',frame)
    c=0
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break