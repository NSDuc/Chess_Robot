# Generated with SMOP  0.41
from libsmop import *
# .\myfast9.m

    
@function
def myfast9(image=None,threshold=None,*args,**kwargs):
    varargin = myfast9.varargin
    nargin = myfast9.nargin

    m,n=size(image,nargout=2)
# .\myfast9.m:2
    corner_cnt=0
# .\myfast9.m:3
    precorners=zeros(0,2)
# .\myfast9.m:4
    corners_map=zeros(m,n)
# .\myfast9.m:5
    scores=zeros(0,0)
# .\myfast9.m:6
    scores_map=zeros(m,n)
# .\myfast9.m:7
    ## FAST角?提取 效果不好
    for i in arange(4,m - 3).reshape(-1):
        for j in arange(4,n - 3).reshape(-1):
            p=image(i,j)
# .\myfast9.m:13
            count=0
# .\myfast9.m:15
            score=0.0
# .\myfast9.m:16
            p1=image(i - 3,j)
# .\myfast9.m:18
            p9=image(i + 3,j)
# .\myfast9.m:19
            if (abs(p1 - p) > threshold):
                count=count + 1
# .\myfast9.m:22
                score=score + abs(p1 - p)
# .\myfast9.m:23
            if (abs(p9 - p) > threshold):
                count=count + 1
# .\myfast9.m:26
                score=score + abs(p9 - p)
# .\myfast9.m:27
            if (count == 0):
                continue
            p5=image(i,j + 3)
# .\myfast9.m:34
            p13=image(i,j - 3)
# .\myfast9.m:35
            if (abs(p5 - p) > threshold):
                count=count + 1
# .\myfast9.m:38
                score=score + abs(p5 - p)
# .\myfast9.m:39
            if (abs(p13 - p) > threshold):
                count=count + 1
# .\myfast9.m:42
                score=score + abs(p13 - p)
# .\myfast9.m:43
            if (count < 3):
                continue
            p2=image(i - 3,j + 1)
# .\myfast9.m:50
            p3=image(i - 2,j + 2)
# .\myfast9.m:51
            p4=image(i - 1,j + 3)
# .\myfast9.m:52
            p6=image(i + 1,j + 3)
# .\myfast9.m:54
            p7=image(i + 2,j + 2)
# .\myfast9.m:55
            p8=image(i + 3,j + 1)
# .\myfast9.m:56
            p10=image(i + 3,j - 1)
# .\myfast9.m:58
            p11=image(i + 2,j - 2)
# .\myfast9.m:59
            p12=image(i + 1,j - 3)
# .\myfast9.m:60
            p14=image(i - 1,j - 3)
# .\myfast9.m:62
            p15=image(i - 2,j - 2)
# .\myfast9.m:63
            p16=image(i - 3,j - 3)
# .\myfast9.m:64
            if (abs(p2 - p) > threshold):
                count=count + 1
# .\myfast9.m:67
                score=score + abs(p2 - p)
# .\myfast9.m:68
            if (abs(p3 - p) > threshold):
                count=count + 1
# .\myfast9.m:71
                score=score + abs(p3 - p)
# .\myfast9.m:72
            if (abs(p4 - p) > threshold):
                count=count + 1
# .\myfast9.m:75
                score=score + abs(p4 - p)
# .\myfast9.m:76
            if (abs(p6 - p) > threshold):
                count=count + 1
# .\myfast9.m:79
                score=score + abs(p6 - p)
# .\myfast9.m:80
            if (abs(p7 - p) > threshold):
                count=count + 1
# .\myfast9.m:83
                score=score + abs(p7 - p)
# .\myfast9.m:84
            if (abs(p8 - p) > threshold):
                count=count + 1
# .\myfast9.m:87
                score=score + abs(p8 - p)
# .\myfast9.m:88
            if (abs(p10 - p) > threshold):
                count=count + 1
# .\myfast9.m:91
                score=score + abs(p10 - p)
# .\myfast9.m:92
            if (abs(p11 - p) > threshold):
                count=count + 1
# .\myfast9.m:95
                score=score + abs(p11 - p)
# .\myfast9.m:96
            if (abs(p12 - p) > threshold):
                count=count + 1
# .\myfast9.m:99
                score=score + abs(p12 - p)
# .\myfast9.m:100
            if (abs(p14 - p) > threshold):
                count=count + 1
# .\myfast9.m:103
                score=score + abs(p14 - p)
# .\myfast9.m:104
            if (abs(p15 - p) > threshold):
                count=count + 1
# .\myfast9.m:107
                score=score + abs(p15 - p)
# .\myfast9.m:108
            if (abs(p16 - p) > threshold):
                count=count + 1
# .\myfast9.m:111
                score=score + abs(p16 - p)
# .\myfast9.m:112
            # FAST9
            if (count < 9):
                continue
            corner_cnt=corner_cnt + 1
# .\myfast9.m:120
            precorners[corner_cnt,1]=i
# .\myfast9.m:121
            precorners[corner_cnt,2]=j
# .\myfast9.m:122
            corners_map[i,j]=1
# .\myfast9.m:123
            scores_map[i,j]=score
# .\myfast9.m:125
            scores[corner_cnt]=score
# .\myfast9.m:127
    
    ## 非极大值抑制
    new_cnt=0
# .\myfast9.m:133
    for k in arange(1,corner_cnt).reshape(-1):
        i=precorners(k,1)
# .\myfast9.m:135
        j=precorners(k,2)
# .\myfast9.m:136
        ts=scores(k)
# .\myfast9.m:137
        ok=1
# .\myfast9.m:139
        for p in arange(i - 2,i + 2).reshape(-1):
            for q in arange(j - 2,j + 2).reshape(-1):
                if (scores_map(p,q) > ts):
                    ok=0
# .\myfast9.m:144
                    break
            if (ok == 0):
                break
        if (ok == 1):
            new_cnt=new_cnt + 1
# .\myfast9.m:154
            corners[new_cnt,1]=j
# .\myfast9.m:155
            corners[new_cnt,2]=i
# .\myfast9.m:156
    
    return corners
    
if __name__ == '__main__':
    pass
    