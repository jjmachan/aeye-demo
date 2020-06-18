from aeye_lib import Aeye
import cv2
import numpy as np

cap = cv2.VideoCapture('test-videos/football.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    print(frame.shape)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
