import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read() # capture frames
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while(True):

    ret, frame2 = cap.read() # capture frames

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray2, gray1)

    # Display the resulting frame
    cv2.imshow('frame',diff)

    gray1 = gray2
    frame1 = frame2
    

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to scape of imaging
        break

cap.release()
cv2.destroyAllWindows()
