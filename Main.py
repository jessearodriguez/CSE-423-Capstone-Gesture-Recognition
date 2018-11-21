import cv2
import numpy as np
import math
import funccaller
import time
capture = cv2.VideoCapture(2) #set to 0 if you only have 1 camera connected.
threshold = 0;
pastdefects =0;
caller = funccaller.caller

ltime = time.time() #last time initialization for stopping continuous function spam
while capture.isOpened():

    #parameters tested using a kinect camera, will probably need to modify for a better one

    #image processing

    ret, frame = capture.read()
    #x,y, y starts at 0 from top
    cv2.rectangle(frame,(300,100),(600,300),(250,0,0))
    roi = frame[100:300,300:600] #point (100,300) to point (300,600)


    blur = cv2.blur(roi, (5, 5)) #1st nosie reduction

    bw = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY) #convert to black and white
    bw = cv2.dilate(bw, (3,3), iterations = 4)
    blur2 = cv2.GaussianBlur(bw, (5, 5), 0) #second noise reduction
    blur2 = cv2.GaussianBlur(bw, (5, 5), 0)  # second noise reduction

    ret,thresh = cv2.threshold(blur2,140,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #finds contours

    marea = 0 # max area
    ci=0 #countour index

    for i in range(len(contours)): #iterates through the total number of different objects found
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area > marea: #finds the biggest contours and stores it, probably need to get a better background/camera for testing
            marea = area
            ci = i
        cnt = contours[ci]

    hull = cv2.convexHull(cnt)


    detected = np.zeros(frame.shape, np.uint8) #blank image used to display only detected contours initialized based off original image size

    #cv2.drawContours(detected, [cnt], 0, (255, 0, 0), 2)

    #cv2.drawContours(detected, [hull], 0, (0, 0, 255), 2)

    cv2.drawContours(frame, [cnt], 0, (255,0, 0), 2, offset = (300,100)) #draws max contour on original image
    #cv2.drawContours(frame, [hull], 0, (0, 0, 255), 2)



    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)

    numofdefects = 0
    if defects is not None: #error checking for blank roi
        for i in range(defects.shape[0]): #taken from opencv defect finding documentation https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
            s, e, f, d = defects [i,0] #start point, end point, farthest point, approximate distance to farthest point

            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])



            if d >1000: #if distance from hull is greater than 200
                cv2.line(roi,start,end,[0,255,0],2) #draws a line between the start and end of all contour defects
                cv2.circle(roi,far,5,[0,0,255],-1)
                numofdefects =numofdefects+1







    cv2.imshow('input', thresh)

    cv2.imshow('image', frame)

    cv2.imshow('roi',thresh)



    if pastdefects == numofdefects:
        threshold = threshold +1
    else:
        threshold = 0

    if threshold >10: #threshold needed to be met before gesture is associated
        print(numofdefects) #using the resultant number to assosciate with gestures to execute functions using a gigantic switch statement
        threshold = 0

        if(time.time()-ltime > .5): #max of 2 actions being executed per second, prevents extreme rapid changes to volume, song skip, ect
            caller.call(numofdefects)
            ltime = time.time()





    pastdefects = numofdefects





    k = cv2.waitKey(10)

    if k == 27: break