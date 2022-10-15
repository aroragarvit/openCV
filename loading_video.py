import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)# 0 is the default camera
# save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # convert to grayscale

    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() # release the camera
out.release() # release the video
cv2.destroyAllWindows()# destroy all windows
