function [result,cnt]=Harris(in_image)
% 功能：檢測影象harris角點
% in_image-待檢測的rgb影象陣列
% a--角點引數響應，取值範圍：0.04~0.06
% [posr，posc]-角點座標
%in_image=rgb2gray(in_image);
I=double(in_image);
[m,n] = size(I);
%%%%計算xy方向梯度%%%%%

fx=[-1,0,1];%x方向梯度模板
Ix=filter2(fx,I);%x方向濾波
fy=[-1;0;1];%y方向梯度模板(注意是分號)
Iy=filter2(fy,I);
%%%%計算兩個方向梯度的乘積%%%%%
Ix2=Ix.^2;
Iy2=Iy.^2;
Ixy=Ix.*Iy;
%%%%使用高斯加權函式對梯度乘積進行加權%%%%
%產生一個7*7的高斯窗函式，sigma值為2
h=fspecial('gaussian',[3,3],2);
IX2=filter2(h,Ix2);
IY2=filter2(h,Iy2);
IXY=filter2(h,Ixy);
%%%%%計算每個像元的Harris響應值%%%%%
[height,width]=size(I);
R=zeros(height,width);
%畫素(i,j)處的Harris響應值
a = 0.06;
for i=1:height
    for j=1:width
        M=[IX2(i,j) IXY(i,j);IXY(i,j) IY2(i,j)];
        R(i,j)=det(M)-a*(trace(M))^2;
    end
end
%%%%%去掉小閾值的Harris值%%%%%
Rmax=max(max(R));
%閾值
t=0.005*Rmax;
for i=1:height
    for j=1:width
        if R(i,j)<t
            R(i,j)=0;
        end
    end
end
%%%%%進行3*3領域非極大值抑制%%%%%%%%%
corner_peaks=imregionalmax(R);
%imregionalmax對二維圖片，採用8領域（預設，也可指定）查詢極值，三維圖片採用26領域
%極值置為1，其餘置為0
num=sum(sum(corner_peaks));
%%%%%%顯示所提取的Harris角點%%%%

decorner_peaks = zeros(m,n);
decorner_peaks(6:m-6,6:n-6) = corner_peaks(6:m-6,6:n-6);
cnt=sum(sum(decorner_peaks));
result=decorner_peaks;
result(result == 1) = 255;
%}

%cnt=num;
%result=double(corner_peaks);
%result(result == 1) = 255;

end