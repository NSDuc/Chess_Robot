# Generated with SMOP  0.41
from libsmop import *
# .\changename.m

    clear
    clc
    path='D:\nntest\chess\redmove_r\ØX_2\'
# .\changename.m:2
    newpath='D:\nntest\chess\redmove_r\new\ØX\'
# .\changename.m:3
    files=dir(strcat(path,'*.jpg'))
# .\changename.m:4
    len_=length(files)
# .\changename.m:5
    for i in arange(1,len_).reshape(-1):
        oldname=files(i).name
# .\changename.m:7
        newname=num2str(i + 11880,'%i.jpg')
# .\changename.m:8
        old=strcat(path,oldname)
# .\changename.m:9
        new=strcat(newpath,newname)
# .\changename.m:10
        copyfile(concat([path,oldname]),concat([newpath,newname]))
    