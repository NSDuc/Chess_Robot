function [result,cnt]=Harris(in_image)
% �\��G�˴��v�Hharris���I
% in_image-���˴���rgb�v�H�}�C
% a--���I�޼��T���A���Ƚd��G0.04~0.06
% [posr�Aposc]-���I�y��
%in_image=rgb2gray(in_image);
I=double(in_image);
[m,n] = size(I);
%%%%�p��xy��V���%%%%%

fx=[-1,0,1];%x��V��׼ҪO
Ix=filter2(fx,I);%x��V�o�i
fy=[-1;0;1];%y��V��׼ҪO(�`�N�O����)
Iy=filter2(fy,I);
%%%%�p���Ӥ�V��ת����n%%%%%
Ix2=Ix.^2;
Iy2=Iy.^2;
Ixy=Ix.*Iy;
%%%%�ϥΰ����[�v�禡���׭��n�i��[�v%%%%
%���ͤ@��7*7���������禡�Asigma�Ȭ�2
h=fspecial('gaussian',[3,3],2);
IX2=filter2(h,Ix2);
IY2=filter2(h,Iy2);
IXY=filter2(h,Ixy);
%%%%%�p��C�ӹ�����Harris�T����%%%%%
[height,width]=size(I);
R=zeros(height,width);
%�e��(i,j)�B��Harris�T����
a = 0.06;
for i=1:height
    for j=1:width
        M=[IX2(i,j) IXY(i,j);IXY(i,j) IY2(i,j)];
        R(i,j)=det(M)-a*(trace(M))^2;
    end
end
%%%%%�h���p�H�Ȫ�Harris��%%%%%
Rmax=max(max(R));
%�H��
t=0.005*Rmax;
for i=1:height
    for j=1:width
        if R(i,j)<t
            R(i,j)=0;
        end
    end
end
%%%%%�i��3*3���D���j�ȧ��%%%%%%%%%
corner_peaks=imregionalmax(R);
%imregionalmax��G���Ϥ��A�ĥ�8���]�w�]�A�]�i���w�^�d�߷��ȡA�T���Ϥ��ĥ�26���
%���ȸm��1�A��l�m��0
num=sum(sum(corner_peaks));
%%%%%%��ܩҴ�����Harris���I%%%%

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