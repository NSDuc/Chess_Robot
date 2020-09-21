# Generated with SMOP  0.41
from libsmop import *
# .\rotate.m

    clear
    clc
    str1='D:\nntest\chess\new_red\ØX\'
# .\rotate.m:2
    str3='.jpg'
# .\rotate.m:2
    for k in 5402.reshape(-1):
        str2=num2str(k)
# .\rotate.m:4
        SC=concat([str1,str2,str3])
# .\rotate.m:5
        i=imread(SC)
# .\rotate.m:6
        #i=imcomplement(i);
        l,m=size(i,nargout=2)
# .\rotate.m:9
        for n in arange(4,356,4).reshape(-1):
            j=imrotate(i,n,'bilinear','crop')
# .\rotate.m:11
            imwrite(j,concat([str1,num2str(k + n / 2),'.jpg']),'quality',100)
    
    #figure