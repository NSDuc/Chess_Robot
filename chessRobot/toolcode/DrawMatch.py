# Generated with SMOP  0.41
from libsmop import *
# .\DrawMatch.m

    
@function
def DrawMatch(Img1=None,m1=None,Img2=None,m2=None,*args,**kwargs):
    varargin = DrawMatch.varargin
    nargin = DrawMatch.nargin

    #DRAWMATCH
    x1,y1=size(Img1,nargout=2)
# .\DrawMatch.m:3
    x2,y2=size(Img2,nargout=2)
# .\DrawMatch.m:4
    x=max(x1,x2)
# .\DrawMatch.m:5
    Img=zeros(x,y1 + y2)
# .\DrawMatch.m:6
    Img[arange(1,x1),arange(1,y1)]=Img1
# .\DrawMatch.m:7
    Img[arange(1,x2),arange(y1 + 1,y2 + y1)]=Img2
# .\DrawMatch.m:8
    figure
    imshow(uint8(Img))
    for n in arange(1,length(m1)).reshape(-1):
        hold('on')
        plot(m1(2,n),m1(1,n),'r+')
        plot(y1 + m2(2,n),m2(1,n),'r+')
        S=concat([m1(2,n),y1 + m2(2,n)])
# .\DrawMatch.m:14
        T=concat([m1(1,n),m2(1,n)])
# .\DrawMatch.m:15
        line(S,T)
    
    hold('off')
    return
    
if __name__ == '__main__':
    pass
    