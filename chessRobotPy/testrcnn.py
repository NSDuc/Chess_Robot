# Generated with SMOP  0.41
from libsmop import *
# .\testrcnn.m

img=imread('stop sign2.jpg')
# .\testrcnn.m:1
bbox,score,label=detect(rcnn,img,'MiniBatchSize',32,nargout=3)
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