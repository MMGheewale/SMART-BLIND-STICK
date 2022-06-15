# import the necessary packages
from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2

print("[INFO] starting video file thread...")
fvs = FileVideoStream(0).start()
time.sleep(1.0)
fps = FPS().start()
# loop over frames from the video file stream
while fvs.more():
    frame = fvs.read()
    frame = imutils.resize(frame, width=450)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame, frame, frame])
    cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    fps.update()
