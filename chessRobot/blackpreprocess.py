import cv2
import numpy as np

def blackpreprocess(gray=None):
    #level = graythresh(gray)
    level = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    bw    = cv2.threshold(gray, level, 255, cv2.THRESH_BINARY)[1]
    
    se_sz = 3;
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*se_sz-1, 2*se_sz-1))

    openbw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, se)

    bw2 = 255 - openbw

    mask = np.multiply(np.ones((gray.shape[0], gray.shape[1])), bw2)
    mask = mask.astype(np.uint8)

    PP = np.multiply(gray,mask)
    t = np.linspace(0, 2*np.pi, 50)
    r = 35
    c = np.array([45,45])
    BW = poly2mask(r*np.cos(t)+c[0], r*.np.sin(t)+c[1], (90, 90))
    Q = np.multiply(PP,BW) / 255
    T = tabulate(ravel(Q))

    T[1,arange()]=[]

    l,__=size(T,nargout=2)

    totalpercent=sum(T(arange(),3))

    percent=0

    for i in range(0,l):
        percent = percent + T(i,3)
        if percent > (totalpercent * 0.65):
            break
    
    th=T(i,1)

    Q[Q > th]=0

    Q[Q > 0]=255

    closeQ = cv.morphologyEx(Q, cv.MORPH_CLOSE, se)
    return closeQ