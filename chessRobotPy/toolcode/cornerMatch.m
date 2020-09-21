function [ match_pt1,match_pt2 ] = cornerMatch( img1,img2,result1,result2,cnt1,cnt2)
[r1,c1]=find(result1==255);
[r2,c2]=find(result2==255);
pt1=[r1 c1]; % N*2 matrix
pt2=[r2 c2];
temp_pt2=zeros(size(pt1));
NCC=zeros(cnt1,cnt2);
% since the windows is too big , it is unwise to ignore the edge of img 
% however, it can be complicated to consider edge,so we extend the img
% instead of consider edge 
k=5;

EXimg1=extendimg(img1,k);
EXimg2=extendimg(img2,k);

%EXimg1=img1;
%EXimg2=img2;

%calculate the NCC of each point's 11*11 neighbourhood
for i=1:cnt1
p=pt1(i,1)+k;q=pt1(i,2)+k;
Win1=EXimg1(p-5:p+5,q-5:q+5); % a window 11*11 around the corner in img1
for j=1:cnt2
m=pt2(j,1)+k;n=pt2(j,2)+k;
Win2=EXimg2(m-5:m+5,n-5:n+5);% a window 11*11 around the corner in img2
NCC(i,j)= NCC_cal(Win1,Win2);
end
%NNR=0.8
MAX=max(NCC(i,:)); %max value of each col
[r,c]=find(NCC(i,:)==MAX);
NCC(NCC==MAX)=0;
SEC=max(NCC(i,:));
NNR=double(SEC/MAX);
if NNR<0.8
temp_pt2(i,:)=pt2(c,:);
else
temp_pt2(i,:)=0;
end;
end;

cnt=numel(temp_pt2,temp_pt2~=0)/2;
match_pt1=zeros(cnt,2);
match_pt2=zeros(cnt,2);
j=1;
for i=1:cnt1
if((temp_pt2(i,1)~=0)&&(pt1(i,1)~=0))
match_pt2(j,:)=temp_pt2(i,:);
match_pt1(j,:)=pt1(i,:);
j=j+1;
end;
end;



end
%.................Extend the img ............................
function [ Eximg1 ] = extendimg( img1,k)
[L1,W1]=size(img1);
Eximg1=zeros(L1+2*k+1,W1+2*k+1);
Eximg1(k+1:k+L1,k+1:k+W1)=img1;

Eximg1(1:k,k+1:W1+k)=Eximg1(1:k,1:W1);%extend up
Eximg1(1:L1+k,W1+k+1:W1+2*k+1)=Eximg1(1:L1+k,W1:W1+k);%extend right
Eximg1(L1+k+1:L1+2*k+1,k+1:W1+2*k+1)=Eximg1(L1:L1+k,k+1:W1+2*k+1);%extend down
Eximg1(1:L1+2*k+1,1:k)=Eximg1(1:L1+2*k+1,k+1:2*k);%extend left
end