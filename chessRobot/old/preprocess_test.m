clear;clc;
num = ;
str1 = 'D:\nntest\testimg\test'; str3='.jpg';
str2 = num2str(num);
SC = [str1, str2, str3];
ia = imread(SC);
ia = imresize(ia,[180,180]);
[m,n,~] = size(ia);
gray = rgb2gray(ia);

level=graythresh(gray);
bw = im2bw(gray,level);
se = strel('disk',2);
openbw = imopen(bw,se);
bw2 = imcomplement(openbw);

mask = ones(size(gray)) .* bw2;
mask = uint8(mask);
PP = gray .* mask;
t = linspace(0, 2*pi, 100);
r = 70;
c = [m/2, n/2];
BW = poly2mask(r*cos(t)+c(1), r*sin(t)+c(2), m, n);
Q = immultiply(PP,BW);

T = tabulate(Q(:));
T(1,:) = [];
[l,~] = size(T);
totalpercent = sum(T(:,3));
percent = 0;
for i = 1:l
    percent = percent + T(i,3);
    if percent > totalpercent * 0.65
        break
    end
end
th = T(i,1);
Q(Q > th) = 0;
Q(Q > 0) = 255;
closeQ = imclose(Q,se);

figure(1),imshow(Q);
figure(2),imshow(closeQ);
%imwrite(closeQ,[str1, 'traindata', num2str(num),'.jpg'],'quality',100);