import numpy as np
import cv2
    
def turn_catch(src=None):
    load('camera')
    src=undistortImage(src,cameraParams)
    src=im2double(src)

    #im  = im2double(src)
    im = cv2.normalize(src.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

    height, width, _ = im.shape
    b,g,r = cv2.split(im)
    Recognition = 0.1*r + 0.1*g + 0.8*b
    radrange = 65
    Recognition2= Recognition[560:700, 470:620] * 255
    accum, _, _ = CircularHough_Grd(Recognition2, 35*radrange)
    
    maxvalue = np.amax(accum)
    x1, y1 = np.where(accum == maxvalue)
    tx = x1[0] + 559
    ty = y1[0] + 469
    return tx, ty