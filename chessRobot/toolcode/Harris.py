# Generated with SMOP  0.41
from libsmop import *
# .\Harris.m

    
@function
def Harris(in_image=None,*args,**kwargs):
    varargin = Harris.varargin
    nargin = Harris.nargin

    # 功能：檢測影象harris角點
# in_image-待檢測的rgb影象陣列
# a--角點引數響應，取值範圍：0.04~0.06
# [posr，posc]-角點座標
#in_image=rgb2gray(in_image);
    I=double(in_image)
# .\Harris.m:7
    m,n=size(I,nargout=2)
# .\Harris.m:8
    ####計算xy方向梯度#####
    
    fx=concat([- 1,0,1])
# .\Harris.m:11
    
    Ix=filter2(fx,I)
# .\Harris.m:12
    
    fy=concat([[- 1],[0],[1]])
# .\Harris.m:13
    
    Iy=filter2(fy,I)
# .\Harris.m:14
    ####計算兩個方向梯度的乘積#####
    Ix2=Ix ** 2
# .\Harris.m:16
    Iy2=Iy ** 2
# .\Harris.m:17
    Ixy=multiply(Ix,Iy)
# .\Harris.m:18
    ####使用高斯加權函式對梯度乘積進行加權####
#產生一個7*7的高斯窗函式，sigma值為2
    h=fspecial('gaussian',concat([3,3]),2)
# .\Harris.m:21
    IX2=filter2(h,Ix2)
# .\Harris.m:22
    IY2=filter2(h,Iy2)
# .\Harris.m:23
    IXY=filter2(h,Ixy)
# .\Harris.m:24
    #####計算每個像元的Harris響應值#####
    height,width=size(I,nargout=2)
# .\Harris.m:26
    R=zeros(height,width)
# .\Harris.m:27
    #畫素(i,j)處的Harris響應值
    a=0.06
# .\Harris.m:29
    for i in arange(1,height).reshape(-1):
        for j in arange(1,width).reshape(-1):
            M=concat([[IX2(i,j),IXY(i,j)],[IXY(i,j),IY2(i,j)]])
# .\Harris.m:32
            R[i,j]=det(M) - dot(a,(trace(M)) ** 2)
# .\Harris.m:33
    
    #####去掉小閾值的Harris值#####
    Rmax=max(max(R))
# .\Harris.m:37
    #閾值
    t=dot(0.005,Rmax)
# .\Harris.m:39
    for i in arange(1,height).reshape(-1):
        for j in arange(1,width).reshape(-1):
            if R(i,j) < t:
                R[i,j]=0
# .\Harris.m:43
    
    #####進行3*3領域非極大值抑制#########
    corner_peaks=imregionalmax(R)
# .\Harris.m:48
    #imregionalmax對二維圖片，採用8領域（預設，也可指定）查詢極值，三維圖片採用26領域
#極值置為1，其餘置為0
    num=sum(sum(corner_peaks))
# .\Harris.m:51
    ######顯示所提取的Harris角點####
    
    decorner_peaks=zeros(m,n)
# .\Harris.m:54
    decorner_peaks[arange(6,m - 6),arange(6,n - 6)]=corner_peaks(arange(6,m - 6),arange(6,n - 6))
# .\Harris.m:55
    cnt=sum(sum(decorner_peaks))
# .\Harris.m:56
    result=copy(decorner_peaks)
# .\Harris.m:57
    result[result == 1]=255
# .\Harris.m:58
    #}
    
    #cnt=num;
#result=double(corner_peaks);
#result(result == 1) = 255;
    
    return result,cnt
    
if __name__ == '__main__':
    pass
    