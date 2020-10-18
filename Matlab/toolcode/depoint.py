# Generated with SMOP  0.41
from libsmop import *
# .\depoint.m

    clear
    clc
    for num in arange(1,900).reshape(-1):
        #num = 1;
        k=11700
# .\depoint.m:4
        str1='D:\nntest\chess\redmove_r\new\ØX\'
# .\depoint.m:5
        str4='.jpg'
# .\depoint.m:5
        str3=num2str(num + k)
# .\depoint.m:6
        SC=concat([str1,str3,str4])
# .\depoint.m:7
        ia=imread(SC)
# .\depoint.m:8
        #inew = zeros(90, 90);
        inew=im2double(ia)
# .\depoint.m:10
        inew[inew > 0.2]=1
# .\depoint.m:11
        inew[inew <= 0.2]=0
# .\depoint.m:12
        ss='D:\nntest\chess\sdepoint_r\ØX\'
# .\depoint.m:13
        imwrite(inew,concat([ss,num2str(num + k),'.jpg']),'quality',100)
    
    #figure(1), imshow(ia);
#figure(2), imshow(inew);