import cv2
import numpy

capture = cv2.VideoCapture(2) #set to 0 if you only have 1 camera connected.

while capture.isOpened():

    #parameters tested using a kinect camera, will probably need to modify for a better one

    #image processing

    ret, frame = capture.read()

    k = cv2.waitKey(10)

    if k ==27: break

    blur = cv2.blur(frame, (3, 3)) #1st nosie reduction

    bw = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY) #convert to black and white

    blur2 = cv2.GaussianBlur(bw, (3, 3),0) #second noise reduction

    ret,thresh = cv2.threshold(blur2,140,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    cv2.imshow('input', thresh)

    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #finds contours and omits the other two vars

    marea = 0
    ci=0
    for i in range(len(contours)): #iterates through the total number of different objects found
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area > marea: #finds the biggest contours and stores it, probably need to get a better background/camera for testing
            marea = area
            ci = i
        cnt = contours[ci]

    hull = cv2.convexHull(cnt)

    drawing = numpy.zeros(frame.shape, numpy.uint8) #blank image used to display only detected contours initialized based off original image size
    print(len(contours))
    cv2.drawContours(drawing, [cnt], 0, (255, 0, 0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)

    cv2.drawContours(frame, [cnt], 0, (255,0, 0), 2) #draws max contour on original image
    cv2.drawContours(frame, [hull], 0, (0, 0, 255), 2)

    cv2.imshow('contour only', drawing)
    cv2.imshow('image', frame)

    #still need to add in how to count the corners needed for gesture recognition