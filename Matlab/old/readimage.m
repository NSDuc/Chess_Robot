clear;clc;
num = 2626;
str1 = 'D:\nntest\chess\red\§L\'; str4='.jpg';
str3 = num2str(num);
SC = [str1, str3, str4];
ia = imread(SC);
figure(1), imshow(ia);