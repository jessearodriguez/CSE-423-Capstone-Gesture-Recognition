import cv2
import numpy

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow('input', frame)
    k = cv2.waitKey(10)

