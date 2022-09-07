# 0201.py
import cv2
import numpy as np

imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE

##encode_img = np.fromfile(imageFile, np.uint8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)
pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
cv2.line(img, (0, 0), (0, 500), (255, 0, 0), 5)
cv2.line(img, (0, 0), (500, 0), (0,0,255), 5)

cv2.imshow('img', img)
#cv2.imshow('Lena color',img)
#cv2.imshow('Lena grayscale',img2)

cv2.waitKey()
cv2.destroyAllWindows()

