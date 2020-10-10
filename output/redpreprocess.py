import cv2
import numpy as np

def redpreprocess(gray=None):
    thresh, a = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    _ , bw = cv2.threshold (gray, thresh*0.72, 255, cv2.THRESH_BINARY)
    bw = 255 - bw

    se = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]], np.uint8)
    openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)
  
    mask = np.ones(gray.shape) * openbw
    mask = mask / 255
    mask = mask.astype(np.uint8)
  
    PP = gray * mask
  
    BW_circle = np.zeros((90, 90))
    BW_circle = cv2.circle(BW_circle, (45, 45), 35, (255, 255, 255), -1)
    BW_circle = BW_circle / 255
    BW = BW_circle.astype(np.uint8).copy()
    Q = PP * BW

    unique_elements, counts_elements = np.unique(Q.flatten(), return_counts=True)
    unique_elements = np.delete(unique_elements, [0])
    counts_elements = np.delete(counts_elements, [0])
    totalpercent = np.sum(counts_elements)
    l = unique_elements.size
    percent = 0
    for i in range(0,l):
        percent = percent + counts_elements[i]
        if float(percent) > (float(totalpercent)*0.66):
            break
    th=unique_elements[i]
  
    Q[Q > th] = 0
    Q[Q > 0]  = 255
  
    bw_chess = cv2.morphologyEx(Q, cv2.MORPH_CLOSE, se)
    return bw_chess