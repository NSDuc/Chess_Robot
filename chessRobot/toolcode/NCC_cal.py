# Generated with SMOP  0.41
from libsmop import *
# .\NCC_cal.m

    
@function
def NCC_cal(I1=None,I2=None,*args,**kwargs):
    varargin = NCC_cal.varargin
    nargin = NCC_cal.nargin

    #UNTITLED2 Summary of this function goes here
#Detailed explanation goes here
    N1=I1 - mean(ravel(I1))
# .\NCC_cal.m:4
    N2=I2 - mean(ravel(I2))
# .\NCC_cal.m:6
    M1=sum(sum(multiply(N1,N2)))
# .\NCC_cal.m:8
    M2=sqrt(dot(sum(sum(N1 ** 2)),sum(sum(N1 ** 2))))
# .\NCC_cal.m:10
    NCC=abs(M1 / M2)
# .\NCC_cal.m:12
    return NCC
    
if __name__ == '__main__':
    pass
    