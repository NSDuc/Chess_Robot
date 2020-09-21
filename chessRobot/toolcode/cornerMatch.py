# Generated with SMOP  0.41
from libsmop import *
# .\cornerMatch.m

    
@function
def cornerMatch(img1=None,img2=None,result1=None,result2=None,cnt1=None,cnt2=None,*args,**kwargs):
    varargin = cornerMatch.varargin
    nargin = cornerMatch.nargin

    r1,c1=find(result1 == 255,nargout=2)
# .\cornerMatch.m:2
    r2,c2=find(result2 == 255,nargout=2)
# .\cornerMatch.m:3
    pt1=concat([r1,c1])
# .\cornerMatch.m:4
    
    pt2=concat([r2,c2])
# .\cornerMatch.m:5
    temp_pt2=zeros(size(pt1))
# .\cornerMatch.m:6
    NCC=zeros(cnt1,cnt2)
# .\cornerMatch.m:7
    # since the windows is too big , it is unwise to ignore the edge of img 
# however, it can be complicated to consider edge,so we extend the img
# instead of consider edge
    k=5
# .\cornerMatch.m:11
    EXimg1=extendimg(img1,k)
# .\cornerMatch.m:13
    EXimg2=extendimg(img2,k)
# .\cornerMatch.m:14
    #EXimg1=img1;
#EXimg2=img2;
    
    #calculate the NCC of each point's 11*11 neighbourhood
    for i in arange(1,cnt1).reshape(-1):
        p=pt1(i,1) + k
# .\cornerMatch.m:21
        q=pt1(i,2) + k
# .\cornerMatch.m:21
        Win1=EXimg1(arange(p - 5,p + 5),arange(q - 5,q + 5))
# .\cornerMatch.m:22
        for j in arange(1,cnt2).reshape(-1):
            m=pt2(j,1) + k
# .\cornerMatch.m:24
            n=pt2(j,2) + k
# .\cornerMatch.m:24
            Win2=EXimg2(arange(m - 5,m + 5),arange(n - 5,n + 5))
# .\cornerMatch.m:25
            NCC[i,j]=NCC_cal(Win1,Win2)
# .\cornerMatch.m:26
        #NNR=0.8
        MAX=max(NCC(i,arange()))
# .\cornerMatch.m:29
        r,c=find(NCC(i,arange()) == MAX,nargout=2)
# .\cornerMatch.m:30
        NCC[NCC == MAX]=0
# .\cornerMatch.m:31
        SEC=max(NCC(i,arange()))
# .\cornerMatch.m:32
        NNR=double(SEC / MAX)
# .\cornerMatch.m:33
        if NNR < 0.8:
            temp_pt2[i,arange()]=pt2(c,arange())
# .\cornerMatch.m:35
        else:
            temp_pt2[i,arange()]=0
# .\cornerMatch.m:37
    
    cnt=numel(temp_pt2,temp_pt2 != 0) / 2
# .\cornerMatch.m:41
    match_pt1=zeros(cnt,2)
# .\cornerMatch.m:42
    match_pt2=zeros(cnt,2)
# .\cornerMatch.m:43
    j=1
# .\cornerMatch.m:44
    for i in arange(1,cnt1).reshape(-1):
        if ((temp_pt2(i,1) != 0) and (pt1(i,1) != 0)):
            match_pt2[j,arange()]=temp_pt2(i,arange())
# .\cornerMatch.m:47
            match_pt1[j,arange()]=pt1(i,arange())
# .\cornerMatch.m:48
            j=j + 1
# .\cornerMatch.m:49
    
    return match_pt1,match_pt2
    
if __name__ == '__main__':
    pass
    
    #.................Extend the img ............................
    
@function
def extendimg(img1=None,k=None,*args,**kwargs):
    varargin = extendimg.varargin
    nargin = extendimg.nargin

    L1,W1=size(img1,nargout=2)
# .\cornerMatch.m:58
    Eximg1=zeros(L1 + dot(2,k) + 1,W1 + dot(2,k) + 1)
# .\cornerMatch.m:59
    Eximg1[arange(k + 1,k + L1),arange(k + 1,k + W1)]=img1
# .\cornerMatch.m:60
    Eximg1[arange(1,k),arange(k + 1,W1 + k)]=Eximg1(arange(1,k),arange(1,W1))
# .\cornerMatch.m:62
    
    Eximg1[arange(1,L1 + k),arange(W1 + k + 1,W1 + dot(2,k) + 1)]=Eximg1(arange(1,L1 + k),arange(W1,W1 + k))
# .\cornerMatch.m:63
    
    Eximg1[arange(L1 + k + 1,L1 + dot(2,k) + 1),arange(k + 1,W1 + dot(2,k) + 1)]=Eximg1(arange(L1,L1 + k),arange(k + 1,W1 + dot(2,k) + 1))
# .\cornerMatch.m:64
    
    Eximg1[arange(1,L1 + dot(2,k) + 1),arange(1,k)]=Eximg1(arange(1,L1 + dot(2,k) + 1),arange(k + 1,dot(2,k)))
# .\cornerMatch.m:65
    
    return Eximg1
    
if __name__ == '__main__':
    pass
    