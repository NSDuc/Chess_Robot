import numpy as np
import cv2
    
def catchroi(src=None):
    b,g,r = cv2.split (src)

    recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)

    thresh, a = cv2.threshold(recognition, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    _ , bw = cv2.threshold (recognition, thresh*0.72, 255, cv2.THRESH_BINARY)
    bw = 255 - bw

    se = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]], np.uint8)
    #se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)

    stats = regionprops(openbw,'basic')
    c = np.concentrate(1, stats.BoundingBox)

    selc = np.where(
        np.abs(c[:,2] - c[:,3]) <= 20 && (c[:,3] >= 75) && (c[:,3] <= 120)
    )

    center = np.concentrate(1,stats.Centroid)
    center = np.fix(center[selc,:])
    for i in range(0, selc.size):
        if (c[selc[i],3] - (center[i,1] - c[selc[i],1])*2) > 5:
            c[selc[i],3] = c[selc[i],3] - (c[selc[i],3] - (center[i,1] - c[selc[i],1])*2) + 1
    
    for i in range(0, selc.size):
        if c[selc[i],3] - (center[i,1] - c[selc[i],1])*2 > 5:
            c[selc[i],3] = c[selc[i],3] - c[selc[i],3] - (center[i,2] - c[selc[i],2])*2 + 1
 
    posX = center[:,0]
    posY = center[:,1]
    
    return c,selc,posX,posY,openbw,src
    