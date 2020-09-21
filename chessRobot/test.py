# Generated with SMOP  0.41
from libsmop import *
# test.m

    clear
    clc
    num=2
# test.m:2
    str1='C:\nntest\testimg\test\test'
# test.m:3
    str3='_1'
# test.m:3
    str4='.jpg'
# test.m:3
    str2=num2str(num)
# test.m:4
    src0=imread(concat([str1,str2,str3,str4]))
# test.m:5
    src1=im2double(src0)
# test.m:6
    src=im2uint8(src1)
# test.m:7
    img=imresize(src,concat([90,90]))
# test.m:8
    gray=rgb2gray(img)
# test.m:10
    r=img(arange(),arange(),1)
# test.m:11
    g=img(arange(),arange(),2)
# test.m:11
    b=img(arange(),arange(),3)
# test.m:11
    gb=g - b
# test.m:12
    rb=r - b
# test.m:13
    max_gb=max(max(gb))
# test.m:14
    max_rb=max(max(rb))
# test.m:14
    if (max_rb > max_gb and max_rb > 40):
        x='red'
# test.m:17
        Q=redpreprocess(gray)
# test.m:18
        load(fullfile('C:\','nntest','red5.mat'))
        predictedLabel=red5.classify(Q)
# test.m:20
    else:
        if (max_gb > max_rb and max_gb > 40):
            x='back'
# test.m:22
            predictedLabel='back'
# test.m:23
        else:
            x='black'
# test.m:25
            Q=blackpreprocess(gray)
# test.m:26
            load(fullfile('C:\','nntest','black2.mat'))
            predictedLabel=black2.classify(Q)
# test.m:28
    
    figure(1)
    imshow(Q)
    title(char(predictedLabel))