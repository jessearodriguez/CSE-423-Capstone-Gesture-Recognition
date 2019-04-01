import cv2
import numpy as np
import math
import funccaller
import time
from darkflow.net.build import TFNet

options = {
    'model': 'cfg/tiny-yolo-voc-11c.cfg',
    'load': 52250,
    'threshold': 0.1,
    'gpu': 0.7
}
tfnet = TFNet(options)

video = cv2.VideoCapture(0)
colors = [tuple(255 * np.random.rand(3)) for _ in range(11)]
caller = funccaller.caller

ltime = time.time()
while True:
    stime = time.time()

    ret, frame = video.read()
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


            if (time.time() - ltime > .5):  # max of 2 actions being executed per second, prevents extreme rapid changes to volume, song skip, ect
                caller.call(label)
                ltime = time.time()


        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
