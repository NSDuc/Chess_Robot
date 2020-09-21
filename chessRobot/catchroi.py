# Generated with SMOP  0.41
from libsmop import *
# .\catchroi.m

    
@function
def catchroi(src=None,*args,**kwargs):
    varargin = catchroi.varargin
    nargin = catchroi.nargin

    #UNTITLED Summary of this function goes here
#   Detailed explanation goes here
    load('camera')
    src=undistortImage(src,cameraParams)
# .\catchroi.m:5
    im=im2double(src)
# .\catchroi.m:6
    height,width,__=size(im,nargout=3)
# .\catchroi.m:7
    b=im(arange(),arange(),3)
# .\catchroi.m:8
    r=im(arange(),arange(),1)
# .\catchroi.m:9
    g=im(arange(),arange(),2)
# .\catchroi.m:10
    Recognition=dot(0.1,r) + dot(0.1,g) + dot(0.8,b)
# .\catchroi.m:11
    #b = im(:,:,3);
#Recognition = b;
    
    level=graythresh(Recognition)
# .\catchroi.m:15
    #bw = im2bw(Recognition,level*0.78);
    bw=im2bw(Recognition,dot(level,0.72))
# .\catchroi.m:17
    bw=imcomplement(bw)
# .\catchroi.m:18
    se=strel('disk',2)
# .\catchroi.m:19
    openbw=imclose(bw,se)
# .\catchroi.m:20
    stats=regionprops(openbw,'basic')
# .\catchroi.m:22
    c=cat(1,stats.BoundingBox)
# .\catchroi.m:24
    selc=find(abs(c(arange(),3) - c(arange(),4)) <= logical_and(20,c(arange(),3)) >= logical_and(75,c(arange(),3)) <= 120)
# .\catchroi.m:25
    #assignin('base','c',c);
#assignin('base','y',y);
    
    center=cat(1,stats.Centroid)
# .\catchroi.m:29
    center=fix(center(selc,arange()))
# .\catchroi.m:30
    for i in arange(1,size(selc)).reshape(-1):
        if c(selc(i),3) - dot((center(i,1) - c(selc(i),1)),2) > 5:
            c[selc(i),3]=c(selc(i),3) - (c(selc(i),3) - dot((center(i,1) - c(selc(i),1)),2)) + 1
# .\catchroi.m:34
            #    c(selc(i),3) = c(selc(i),3) - (c(selc(i),3) - (c(selc(i),1) + c(selc(i),3) - center(i,1))*2) + 1;
    #    c(selc(i),1) = c(selc(i),1) + (c(selc(i),3) - (c(selc(i),1) + c(selc(i),3) - center(i,1))*2) - 1;
    
    for i in arange(1,size(selc)).reshape(-1):
        if c(selc(i),4) - dot((center(i,2) - c(selc(i),2)),2) > 5:
            c[selc(i),4]=c(selc(i),4) - (c(selc(i),4) - dot((center(i,2) - c(selc(i),2)),2)) + 1
# .\catchroi.m:43
            #    c(selc(i),4) = c(selc(i),4) - (c(selc(i),4) - (c(selc(i),2) + c(selc(i),4) - center(i,2))*2) + 1;
    #    c(selc(i),2) = c(selc(i),2) + (c(selc(i),4) - (c(selc(i),2) + c(selc(i),4) - center(i,2))*2) - 1;
    
    #{
    regionXb=c(selc,1)
# .\catchroi.m:52
    regionXe=c(selc,1) + c(selc,3)
# .\catchroi.m:53
    regionYb=c(selc,2)
# .\catchroi.m:54
    regionYe=c(selc,2) + c(selc,4)
# .\catchroi.m:55
    for i in arange(1,size(selc)).reshape(-1):
        eval(concat(['roi',num2str(i),'= src(regionYb(',num2str(i),'):regionYe(',num2str(i),'),regionXb(',num2str(i),'):regionXe(',num2str(i),'),:);']))
        eval(concat(['assignin('base','roi',roi',num2str(i),');']))
    
    #}
#for i=1:size(selc)
#    roi = roi1;
#end
#roi = roi1;
    posX=center(arange(),1)
# .\catchroi.m:67
    posY=center(arange(),2)
# .\catchroi.m:68
    #roi = src(regionYb:regionYe,regionXb:regionXe,:);
#posX = c(y,1) + c(y,3) * 0.5;
#posY = c(y,2) + c(y,4) * 0.5;
#assignin('base','roi',roi);
    
    return c,selc,posX,posY,openbw,src
    
if __name__ == '__main__':
    pass
    