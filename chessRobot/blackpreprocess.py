# Generated with SMOP  0.41
from libsmop import *
# .\blackpreprocess.m

    
@function
def blackpreprocess(gray=None,*args,**kwargs):
    varargin = blackpreprocess.varargin
    nargin = blackpreprocess.nargin

    level=graythresh(gray)
# .\blackpreprocess.m:2
    bw=im2bw(gray,level)
# .\blackpreprocess.m:3
    se=strel('disk',2)
# .\blackpreprocess.m:4
    openbw=imopen(bw,se)
# .\blackpreprocess.m:5
    bw2=imcomplement(openbw)
# .\blackpreprocess.m:6
    mask=multiply(ones(size(gray)),bw2)
# .\blackpreprocess.m:8
    mask=uint8(mask)
# .\blackpreprocess.m:9
    PP=multiply(gray,mask)
# .\blackpreprocess.m:10
    t=linspace(0,dot(2,pi),50)
# .\blackpreprocess.m:11
    r=35
# .\blackpreprocess.m:12
    c=concat([45,45])
# .\blackpreprocess.m:13
    BW=poly2mask(dot(r,cos(t)) + c(1),dot(r,sin(t)) + c(2),90,90)
# .\blackpreprocess.m:14
    Q=immultiply(PP,BW)
# .\blackpreprocess.m:15
    T=tabulate(ravel(Q))
# .\blackpreprocess.m:17
    T[1,arange()]=[]
# .\blackpreprocess.m:18
    l,__=size(T,nargout=2)
# .\blackpreprocess.m:19
    totalpercent=sum(T(arange(),3))
# .\blackpreprocess.m:20
    percent=0
# .\blackpreprocess.m:21
    for i in arange(1,l).reshape(-1):
        percent=percent + T(i,3)
# .\blackpreprocess.m:23
        if percent > dot(totalpercent,0.65):
            break
    
    th=T(i,1)
# .\blackpreprocess.m:28
    Q[Q > th]=0
# .\blackpreprocess.m:29
    Q[Q > 0]=255
# .\blackpreprocess.m:30
    closeQ=imclose(Q,se)
# .\blackpreprocess.m:31
    return closeQ
    
if __name__ == '__main__':
    pass
    