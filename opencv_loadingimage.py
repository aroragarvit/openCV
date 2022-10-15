import cv2
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread("download.jpeg",cv2.IMREAD_GRAYSCALE)
#plt.imshow(img,cmap="gray",interpolation= "bicubic")# plot image using matplotlib
#plt.show()

cv2.line(img,(0,0),(159,117),(0,0,0),10)

cv2.rectangle(img,(15,25),(200,150),(0,255,0),5) 
cv2.imshow("image",img)# plot image using cv2
cv2.waitKey(0)# wait for key press
cv2.destroyAllWindows()# destroy all windows

#cv2.imwrite("download.png",img)# save image

