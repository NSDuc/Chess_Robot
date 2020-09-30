import numpy as np
import cv2
    
def catchroi(src=None):
    #load('camera')
    # camera_matrix
    # distortion_coefficients
    # scaled_camera_matrix
    #src = undistortImage(src,cameraParams)
    src = cv2.undistort(src, camera_matrix, distortion_coefficients, None, scaled_camera_matrix,)

    #im  = im2double(src)
    im = cv2.normalize(im.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

    height, width, _ = im.shape
    
    b,g,r = cv2.split(im)

    Recognition = 0.1*r + 0.1*g + 0.8*b
    
    level = cv.threshold(Recognition,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    bw    = cv2.threshold(gray, level*0.72, 255, cv2.THRESH_BINARY)[1]
    bw    = 255 - bw
    
    #se=strel('disk',2), Không thể convert được giống Matlab hoàn toàn
    #https://stackoverflow.com/questions/29740108/disk-structuring-element-in-opencv
    se_sz = 3;
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*se_sz-1, 2*se_sz-1))

    #openbw=imclose(bw,se)
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
    