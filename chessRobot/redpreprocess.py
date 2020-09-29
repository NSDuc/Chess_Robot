import cv2
import numpy as np
from skimage import draw

def poly2mask(vertex_row_coords, vertex_col_coords, shape):
    fill_row_coords, fill_col_coords = draw.polygon(vertex_row_coords, vertex_col_coords, shape)
    mask = np.zeros(shape, dtype=np.bool)
    mask[fill_row_coords, fill_col_coords] = True
    return mask

def redpreprocess(gray=None):
    radrange = 45
    
    accum = CircularHough_Grd(gray,concat([dot(radrange,0.78),radrange]))
    maxvalue = max(ravel(accum))
    x,y=find(accum == maxvalue,nargout=2)

    #level = graythresh(gray)
    #bw=im2bw(gray,level)
    level = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    bw    = cv2.threshold(gray,level,255,cv2.THRESH_BINARY)[1]
    
    #se=strel('disk',2), Không thể convert được giống Matlab hoàn toàn
    #https://stackoverflow.com/questions/29740108/disk-structuring-element-in-opencv
    se_sz = 3;
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*se_sz-1, 2*se_sz-1))

    #openbw=imopen(bw,se)
    openbw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, se)

    #bw2=imcomplement(openbw)
    bw2 = 255 - openbw

    #mask = ones(size(gray)) .* bw2;
    mask = np.multiply(np.ones((gray.shape[0], gray.shape[1])), bw2)
    mask = mask.astype(np.uint8)

    PP = np.multiply(gray,mask)
    t = np.linspace(0, 2*np.pi, 50)
    r = 35
    c = np.array([45,45])
    
    #BW = poly2mask(r*cos(t)+c(1), r*sin(t)+c(2), 90, 90);
    BW = poly2mask(r*np.cos(t)+c[0], r*np.sin(t)+c[1], (90, 90))
    
    Q = np.multiply(PP,BW) / 255

    T = tabulate(ravel(Q))

    T[0,:] = []
    l, _ = T.size()
    totalpercent=sum(T[:,3])
    percent=0
    for i in range(0,l):
        percent=percent + T[i,3]
        if percent > (totalpercent*0.66):
            break
    
    th=T[i,1]
    Q[Q > th]=0
    Q[Q > 0]=255

    closeQ = cv.morphologyEx(Q, cv.MORPH_CLOSE, se)
    return closeQ

