from darkflow.net.build import TFNet

import cv2

import numpy as np


import time



options = {
    'model': 'cfg/tiny-yolo-voc-11c.cfg',
    'load': 52250,
    'threshold': 0.1,
    'gpu': 0.7
}
tfnet = TFNet(options) #example code based off of https://github.com/markjay4k/YOLO-series/blob/master/part4_video.py



colors = [tuple(255 * np.random.rand(3)) for _ in range(11)]

capture = cv2.VideoCapture(0)

# ALL GESTURES ARE FINIKY IN THEIR DETECTIONS, CURRENTLY UNAVOUDABLE DUE TO TINY YOLO, YOLOV3 NEEDS BETTER HARDWARE
# 3 fingers works at some positions
# camera gesture same as above, harder to do
# closed hand contests with point up for some reason
# handgun works with like 60% detection rate
# ok gesture works
# peace gesture contests too much with point up, <10% detection rate
# point up works
# rock and roll works
# stop gesture contends with rock and roll, 15~% detection rate
# thumbs up works at certain angles
# thumbs down not working at all
while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        print(results)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()