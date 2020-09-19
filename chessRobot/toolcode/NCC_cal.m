function [ NCC ] = NCC_cal(I1,I2 )
%UNTITLED2 Summary of this function goes here
%Detailed explanation goes here
N1=I1-mean(I1(:));

N2=I2-mean(I2(:));

M1=sum(sum(N1.*N2));

M2=sqrt(sum(sum(N1.^2))*sum(sum(N1.^2)));

NCC=abs(M1/M2);

end