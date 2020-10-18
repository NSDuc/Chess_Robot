# Generated with SMOP  0.41
from libsmop import *
# .\fastconert.m

    clear('all')
    close_('all')
    clc
    tic
    img=imread('D:\nntest\testimg\test134_1.jpg')
# .\fastconert.m:5
    imshow(img)
    m,n=size(img,nargout=2)
# .\fastconert.m:8
    score=zeros(m,n)
# .\fastconert.m:9
    t=60
# .\fastconert.m:11
    
    for i in arange(4,m - 3).reshape(-1):
        for j in arange(4,n - 3).reshape(-1):
            p=img(i,j)
# .\fastconert.m:14
            pn=concat([img(i - 3,j),img(i - 3,j + 1),img(i - 2,j + 2),img(i - 1,j + 3),img(i,j + 3),img(i + 1,j + 3),img(i + 2,j + 2),img(i + 3,j + 1),img(i + 3,j),img(i + 3,j - 1),img(i + 2,j - 2),img(i + 1,j - 3),img(i,j - 3),img(i - 1,j - 3),img(i - 2,j - 2),img(i - 3,j - 1)])
# .\fastconert.m:16
            if abs(pn(1) - p) < t and abs(pn(9) - p) < t:
                continue
            #步?3
            p1_5_9_13=concat([abs(pn(1) - p) > t,abs(pn(5) - p) > t,abs(pn(9) - p) > t,abs(pn(13) - p) > t])
# .\fastconert.m:25
            if sum(p1_5_9_13) >= 3:
                ind=find(abs(pn - p) > t)
# .\fastconert.m:27
                if length(ind) >= 9:
                    score[i,j]=sum(abs(pn - p))
# .\fastconert.m:30
    
    #步?5，非极大抑制，并且?出特征?
    for i in arange(4,m - 3).reshape(-1):
        for j in arange(4,n - 3).reshape(-1):
            if score(i,j) != 0:
                if max(max(score(arange(i - 2,i + 2),arange(j - 2,j + 2)))) == score(i,j):
                    img(i - 3,j),img(i - 3,j + 1),img(i - 2,j + 2),img(i - 1,j + 3),img(i,j + 3),img(i + 1,j + 3),img(i + 2,j + 2),img(i + 3,j + 1),img(i + 3,j),img(i + 3,j - 1),img(i + 2,j - 2),img(i + 1,j - 3),img(i,j - 3),img(i - 1,j - 3),img(i - 2,j - 2),img(i - 3,j - 1)=deal(255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,nargout=16)
# .\fastconert.m:42
    
    figure
    imshow(img)
    toc