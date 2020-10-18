# Generated with SMOP  0.41
from libsmop import *
# .\circltest.m

    clear
    clc
    Oimg=imread('D:\nntest\testimg\Picture 180.jpg')
# .\circltest.m:2
    #img = imresize(Oimg,[180,180]);
    img=rgb2gray(Oimg)
# .\circltest.m:4
    m,n=size(img,nargout=2)
# .\circltest.m:5
    #radrange = min(m,n)/2;
    
    tic
    #[accum, circen, cirrad] = CircularHough_Grd(img, [radrange * 0.78, radrange]);
    accum,circen,cirrad=CircularHough_Grd(img,concat([35,65]),nargout=3)
# .\circltest.m:10
    toc
    max=max(ravel(accum))
# .\circltest.m:12
    x,y=find(accum == max,nargout=2)
# .\circltest.m:13
    figure(1)
    imagesc(accum)
    axis('image')
    #figure(2); imagesc(center); axis image;
#title('Accumulation Array from Circular Hough Transform');
#figure(2); imagesc(img); colormap('gray'); axis image;
#hold on;
#plot(circen(:,1), circen(:,2), 'r+');
#for k = 1 : size(circen, 1),
#    DrawCircle(circen(k,1), circen(k,2), cirrad(k), 32, 'b-');
#end
#hold off;
#title(['Raw Image with Circles Detected ', ...
#    '(center positions and radii marked)']);
    figure(3)
    surf(accum,'EdgeColor','none')
    axis('ij')
    #title('3-D View of the Accumulation Array');