import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()

    #Our operations on the frame com ehre
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything done, relesae the capture
cap.release()
cv2.destroyAllWindows()