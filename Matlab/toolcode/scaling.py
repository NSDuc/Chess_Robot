# Generated with SMOP  0.41
from libsmop import *
# .\scaling.m

    clear
    clc
    for k in arange(2201,2380).reshape(-1):
        str1='D:\nntest\chess\red\ØX\'
# .\scaling.m:4
        str3='.jpg'
# .\scaling.m:4
        str2=num2str(k)
# .\scaling.m:5
        SC=concat([str1,str2,str3])
# .\scaling.m:6
        src=imread(SC)
# .\scaling.m:7
        img=imresize(src,concat([90,90]))
# .\scaling.m:8
        ss='D:\nntest\chess\red\90ØX\'
# .\scaling.m:9
        imwrite(img,concat([ss,num2str(k),'.jpg']),'quality',100)
    
    #{
    gray2=im2double(gray)
# .\scaling.m:15
    w2=fspecial('sobel')
# .\scaling.m:16
    
    w3=fliplr(w2.T)
# .\scaling.m:17
    w4=w2.T
# .\scaling.m:18
    w5=flipud(w2)
# .\scaling.m:19
    g2=imfilter(gray2,w2,'replicate')
# .\scaling.m:20
    g3=imfilter(gray2,w3,'replicate')
# .\scaling.m:21
    g4=imfilter(gray2,w4,'replicate')
# .\scaling.m:22
    g5=imfilter(gray2,w5,'replicate')
# .\scaling.m:23
    size=size(img)
# .\scaling.m:25
    sobx=zeros(size)
# .\scaling.m:26
    sobn=zeros(size)
# .\scaling.m:27
    sobx=max(max(max(g2,g3),g4),g5)
# .\scaling.m:28
    sobn=min(min(min(g2,g3),g4),g5)
# .\scaling.m:29
    figure(3)
    imshow(sobx)
    filsobn=gray2 - sobn
# .\scaling.m:31
    figure(4)
    imshow(filsobn)
    #figure(5), imshow(sobx);
#figure(6), imshow(sobx);
    
    if (max_rb > max_gb and max_rb > 40):
        gray2=im2double(gray)
# .\scaling.m:37
        w=fspecial('sobel')
# .\scaling.m:38
        edge=imfilter(gray2,w,'replicate')
# .\scaling.m:39
        fil=gray2 - edge
# .\scaling.m:40
        medfil=medfilt2(fil)
# .\scaling.m:41
        imwrite(medfil,concat(['beidentified.jpg']),'quality',80)
        identify_img=imread('beidentified.jpg')
# .\scaling.m:43
        load(fullfile('D:\','nntest','red2.mat'))
        predictedLabel=red2.classify(identify_img)
# .\scaling.m:45
    else:
        if (max_gb > max_rb and max_gb > 40):
            predictedLabel='back'
# .\scaling.m:48
        else:
            gray2=im2double(gray)
# .\scaling.m:50
            w=fspecial('sobel')
# .\scaling.m:51
            edge=imfilter(gray2,w,'replicate')
# .\scaling.m:52
            fil=gray2 - edge
# .\scaling.m:53
            medfil=medfilt2(fil)
# .\scaling.m:54
            imwrite(medfil,concat(['beidentified.jpg']),'quality',80)
            identify_img=imread('beidentified.jpg')
# .\scaling.m:56
            load(fullfile('D:\','nntest','black2.mat'))
            predictedLabel=black2.classify(identify_img)
# .\scaling.m:58
    
    #}
#{
    to=linspace(0,dot(2,pi),50)
# .\scaling.m:63
    ro=85
# .\scaling.m:64
    co=concat([90,90])
# .\scaling.m:65
    BWo=poly2mask(dot(ro,cos(to)) + co(1),dot(ro,sin(to)) + co(2),180,180)
# .\scaling.m:66
    ti=linspace(0,dot(2,pi),50)
# .\scaling.m:67
    ri=70
# .\scaling.m:68
    ci=concat([90,90])
# .\scaling.m:69
    BWi=poly2mask(dot(ri,cos(ti)) + ci(1),dot(ri,sin(ti)) + ci(2),180,180)
# .\scaling.m:70
    cir=BWo - BWi
# .\scaling.m:71
    se=translate(strel(1),concat([0,0]))
# .\scaling.m:72
    mcc=imdilate(cir,se)
# .\scaling.m:73
    mcc[mcc == - Inf]=0
# .\scaling.m:74
    cc=multiply(mcc,bw2)
# .\scaling.m:75
    #}