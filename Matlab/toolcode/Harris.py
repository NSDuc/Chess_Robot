# Generated with SMOP  0.41
from libsmop import *
# .\Harris.m

    
@function
def Harris(in_image=None,*args,**kwargs):
    varargin = Harris.varargin
    nargin = Harris.nargin

    # �\��G�˴��v�Hharris���I
# in_image-���˴���rgb�v�H�}�C
# a--���I�޼��T���A���Ƚd��G0.04~0.06
# [posr�Aposc]-���I�y��
#in_image=rgb2gray(in_image);
    I=double(in_image)
# .\Harris.m:7
    m,n=size(I,nargout=2)
# .\Harris.m:8
    ####�p��xy��V���#####
    
    fx=concat([- 1,0,1])
# .\Harris.m:11
    
    Ix=filter2(fx,I)
# .\Harris.m:12
    
    fy=concat([[- 1],[0],[1]])
# .\Harris.m:13
    
    Iy=filter2(fy,I)
# .\Harris.m:14
    ####�p���Ӥ�V��ת����n#####
    Ix2=Ix ** 2
# .\Harris.m:16
    Iy2=Iy ** 2
# .\Harris.m:17
    Ixy=multiply(Ix,Iy)
# .\Harris.m:18
    ####�ϥΰ����[�v�禡���׭��n�i��[�v####
#���ͤ@��7*7���������禡�Asigma�Ȭ�2
    h=fspecial('gaussian',concat([3,3]),2)
# .\Harris.m:21
    IX2=filter2(h,Ix2)
# .\Harris.m:22
    IY2=filter2(h,Iy2)
# .\Harris.m:23
    IXY=filter2(h,Ixy)
# .\Harris.m:24
    #####�p��C�ӹ�����Harris�T����#####
    height,width=size(I,nargout=2)
# .\Harris.m:26
    R=zeros(height,width)
# .\Harris.m:27
    #�e��(i,j)�B��Harris�T����
    a=0.06
# .\Harris.m:29
    for i in arange(1,height).reshape(-1):
        for j in arange(1,width).reshape(-1):
            M=concat([[IX2(i,j),IXY(i,j)],[IXY(i,j),IY2(i,j)]])
# .\Harris.m:32
            R[i,j]=det(M) - dot(a,(trace(M)) ** 2)
# .\Harris.m:33
    
    #####�h���p�H�Ȫ�Harris��#####
    Rmax=max(max(R))
# .\Harris.m:37
    #�H��
    t=dot(0.005,Rmax)
# .\Harris.m:39
    for i in arange(1,height).reshape(-1):
        for j in arange(1,width).reshape(-1):
            if R(i,j) < t:
                R[i,j]=0
# .\Harris.m:43
    
    #####�i��3*3���D���j�ȧ��#########
    corner_peaks=imregionalmax(R)
# .\Harris.m:48
    #imregionalmax��G���Ϥ��A�ĥ�8���]�w�]�A�]�i���w�^�d�߷��ȡA�T���Ϥ��ĥ�26���
#���ȸm��1�A��l�m��0
    num=sum(sum(corner_peaks))
# .\Harris.m:51
    ######��ܩҴ�����Harris���I####
    
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
    