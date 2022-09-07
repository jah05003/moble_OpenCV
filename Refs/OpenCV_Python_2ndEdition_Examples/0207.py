# 0207.py
import cv2
import numpy as np

cap = cv2.VideoCapture('./data/vtest.avi')  # 0번 카메라
##cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)
imageFile = './data/lena.jpg'

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    #글자 출력
    #text = 'OpenCV Programming'
    #org = (50,150)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(frame,text, org, font, 1, (255,0,0), 2)
    
    img  = cv2.imread(imageFile) 
    res = cv2.resize(img, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
    frame = cv2.resize(frame, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
    hap = frame * 0.5 + res * 0.5
    #blended = res * 0.5 + frame * (1-0.5)
    hap = hap.astype(np.uint8)
    cv2.imshow('frame',hap)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
