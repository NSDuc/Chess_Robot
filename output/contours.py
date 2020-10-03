import cv2 
import numpy as np 
  
# Let's load a simple image with 3 black squares 
image = cv2.imread(r'E:\robot_arm\matlab_only\bw100.jpg', 0)
cv2.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(image,  
    cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) 
  
cv2.imshow('Canny Edges After Contouring', image) 
cv2.waitKey(0) 

print("Number of Contours found = " + str(len(contours))) 
print(contours[0])
rects = cv2.boundingRect(contours[0])
# Draw all contours 
# -1 signifies drawing all contours 
i = 0
for con in contours:
    i += 1
    rect = cv2.boundingRect(con)
    if rect[2] > 70 and rect[3] > 70:
        regionXb = rect[0]
        regionXe = rect[0] + rect[2]
        regionYb = rect[1]
        regionYe = rect[1] + rect[3]
        # cv2.drawContours(image, [con], 0, (0, 255, 0), 3) 
        sub_image = image[regionYb:regionYe,regionXb:regionXe]
        cv2.imshow('Contours'+str(i), sub_image) 
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 