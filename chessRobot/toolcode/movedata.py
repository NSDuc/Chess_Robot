# Generated with SMOP  0.41
from libsmop import *
# .\movedata.m

    clear
    clc
    for i in arange(1,4).reshape(-1):
        for num in arange(5401,5580).reshape(-1):
            #num = 1661;
            str1='D:\nntest\chess\new_red\ØX\'
# .\movedata.m:5
            str4='.jpg'
# .\movedata.m:5
            str3=num2str(num)
# .\movedata.m:6
            SC=concat([str1,str3,str4])
# .\movedata.m:7
            ia=imread(SC)
# .\movedata.m:8
            inew=zeros(90,90)
# .\movedata.m:9
            movex=5
# .\movedata.m:10
            movey=5
# .\movedata.m:11
            if i == 1:
                inew[arange(),arange(1 + movey,90)]=ia(arange(),arange(1,90 - movey))
# .\movedata.m:13
                k=180
# .\movedata.m:14
            else:
                if i == 2:
                    inew[arange(),arange(1,90 - movey)]=ia(arange(),arange(1 + movey,90))
# .\movedata.m:16
                    k=360
# .\movedata.m:17
                else:
                    if i == 3:
                        inew[arange(1,90 - movex),arange()]=ia(arange(1 + movex,90),arange())
# .\movedata.m:19
                        k=540
# .\movedata.m:20
                    else:
                        inew[arange(1 + movex,90),arange()]=ia(arange(1,90 - movex),arange())
# .\movedata.m:22
                        k=720
# .\movedata.m:23
            inew=uint8(inew)
# .\movedata.m:25
            ss='D:\nntest\chess\new_red\ØX\'
# .\movedata.m:26
            imwrite(inew,concat([ss,num2str(num + k),'.jpg']),'quality',100)
    
    #figure(1), imshow(ia);
#figure(2), imshow(inew);
#}
#{
    a=concat([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# .\movedata.m:34
    m=size(a)
# .\movedata.m:35
    b=zeros(m)
# .\movedata.m:36
    movex=1
# .\movedata.m:37
    movey=2
# .\movedata.m:38
    #b(:,movey+1:m(2)) = a(:,1:m(2)-movey) #rightmove
#b(:,1:m(2)-movey) = a(:,1+movey:m(2)) #leftmove
#b(1:m(1)-movey,:) = a(1+movey:m(1),:) #upmove
#b(1+movey:m(1),:) = a(1:m(1)-movey,:) #downmove
#}