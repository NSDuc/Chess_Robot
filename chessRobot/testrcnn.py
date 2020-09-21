# Generated with SMOP  0.41
from libsmop import *
import numpy as np
import cv2
# .\testrcnn.m

img = cv2.imread('stop sign2.jpg')
# .\testrcnn.m:1
bbox,score,label=cv2.detect(rcnn,img,'MiniBatchSize',32,nargout=3)
# .\testrcnn.m:3
score,idx=max(score,nargout=2)
# .\testrcnn.m:5
bbox=bbox(idx,arange())
# .\testrcnn.m:7
annotation=sprintf('%s: (Confidence = %f)',label(idx),score)
# .\testrcnn.m:8
detectedImg=insertObjectAnnotation(img,'rectangle',bbox,annotation)
# .\testrcnn.m:10
figure
imshow(detectedImg)