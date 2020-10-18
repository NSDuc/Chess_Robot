# Generated with SMOP  0.41
from libsmop import *
# nntest.m

    #clear;clc
#num = 2;
#str1 = 'D:\nntest\testimg\test'; str3 = '_1'; str4 = '.jpg';
#str2 = num2str(num);
#src = imread([str1 str2 str3 str4]);
#load(fullfile('D:\','nntest','red3.mat'));
    load(fullfile('C:\','nntest','red5.mat'))
    load(fullfile('C:\','nntest','black2.mat'))
    #for i=1:size(selc)
    for i in 1.reshape(-1):
        eval(concat(['cim = im2uint8(roi',num2str(i),');']))
        #cim = imnoise(cim,'salt & pepper',0.02);
        img=imresize(cim,concat([90,90]))
# nntest.m:13
        gray=rgb2gray(img)
# nntest.m:15
        r=img(arange(),arange(),1)
# nntest.m:16
        g=img(arange(),arange(),2)
# nntest.m:16
        b=img(arange(),arange(),3)
# nntest.m:16
        gb=g - b
# nntest.m:17
        rb=r - b
# nntest.m:18
        median_gb=median(median(gb))
# nntest.m:19
        median_rb=median(median(rb))
# nntest.m:19
        if (median_rb > median_gb and median_rb >= 10):
            Q=redpreprocess(gray)
# nntest.m:22
            predictedLabel[i]=red5.classify(Q)
# nntest.m:23
            #    predictedLabel(i) = red4.classify(Q);
        #end
        else:
            if (median_gb > median_rb and median_gb > 15):
                Q=imcomplement(im2bw(gray,0.38))
# nntest.m:28
                predictedLabel[i]=categorical(cellstr('­I­±'))
# nntest.m:29
            else:
                Q=blackpreprocess(gray)
# nntest.m:31
                predictedLabel[i]=black2.classify(Q)
# nntest.m:32
        #end
        figure(i)
        imshow(Q)
        title(char(predictedLabel(i)))
    