# Generated with SMOP  0.41
from libsmop import *
# .\turn_catch.m

    
@function
def turn_catch(src=None,*args,**kwargs):
    varargin = turn_catch.varargin
    nargin = turn_catch.nargin

    load('camera')
    src=undistortImage(src,cameraParams)
# .\turn_catch.m:4
    src=im2double(src)
# .\turn_catch.m:5
    im=im2double(src)
# .\turn_catch.m:7
    height,width,__=size(im,nargout=3)
# .\turn_catch.m:8
    b=im(arange(),arange(),3)
# .\turn_catch.m:9
    r=im(arange(),arange(),1)
# .\turn_catch.m:10
    g=im(arange(),arange(),2)
# .\turn_catch.m:11
    Recognition=dot(0.1,r) + dot(0.1,g) + dot(0.8,b)
# .\turn_catch.m:12
    radrange=65
# .\turn_catch.m:14
    Recognition2=dot((Recognition(arange(560,700),arange(470,620))),255)
# .\turn_catch.m:15
    accum,circen,cirrad=CircularHough_Grd(Recognition2,concat([35,radrange]),nargout=3)
# .\turn_catch.m:16
    maxvalue=max(ravel(accum))
# .\turn_catch.m:17
    x1,y1=find(accum == maxvalue,nargout=2)
# .\turn_catch.m:18
    tx=x1 + 559
# .\turn_catch.m:19
    ty=y1 + 469
# .\turn_catch.m:19
    #{
    figure(1)
    imagesc(accum)
    hold('on')
    plot(ty,tx,'g*')
    t=concat([ty - 40,tx - 40,80,80])
# .\turn_catch.m:24
    rectangle('Position',t(1,arange()),'LineWidth',2,'LineStyle','--','EdgeColor','r')
    hold('off')
    src2=src(arange(500,650),arange(550,700),arange())
# .\turn_catch.m:27
    #}
#roi33 = src(tx-50:tx+49,ty-50:ty+49,:);
#figure(1),imshow(src2);
#figure(2),imshow(roi33);