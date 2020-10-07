import numpy as np
import cv2
    
def turn_catch(src=None):
    b,g,r = cv2.split(im)
    recognition  = 0.1*r + 0.1*g + 0.8*b
    recognition2 = recognition[560:700, 470:620].astype(np.uint8)
    radrange = 65
    accum, _, _ = CircularHough_Grd(recognition2, [35,radrange])
    
    maxvalue = np.amax(accum)
    x1, y1 = np.where(accum == maxvalue)
    tx = x1[0] + 559
    ty = y1[0] + 469
    return tx, ty