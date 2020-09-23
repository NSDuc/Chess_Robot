import cv2

def ConvoNN(roi=None,*args,**kwargs):
    varargin = ConvoNN.varargin
    nargin = ConvoNN.nargin

    load(fullfile('red5.mat'))
    load(fullfile('black2.mat'))

    img  = cv2.resize(roi,(90,90))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b,g,r = cv2.split(img)
    gb = g-b
    rb = r-b
    median_gb=gb.mean()
    median_rb=rb.mean()
    assignin('base','median_rb',median_rb)
    if (median_rb > median_gb and median_rb >= 5):
        Q = redpreprocess(gray)
        predictedLabel = red5.classify(Q)
        if (predictedLabel == 'r¨®') or (predictedLabel == '¥K') or (predictedLabel == '¬¶'):
            predictedLabel = red4.classify(Q)
    elif (median_gb > median_rb and median_gb >= 15):
        thresh = 0.38*255
        im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
        Q = imcomplement(im_bw)
        predictedLabel = categorical(cellstr('­I­±'))
    else:
        Q = blackpreprocess(gray)
        predictedLabel = black2.classify(Q)
    
    assignin('base','predictedLabel',predictedLabel)
    return predictedLabel