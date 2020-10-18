%clear; clc;
load camera;
num = 1;
str1 = 'D:\nntest\testimg\'; str2 = 'Picture '; str4='.jpg';
str3 = num2str(num);
SC = [str1, str2, str3, str4];
src = imread(SC);
src_udt = undistortImage(src,cameraParams);
figure(1),imshow(src_udt)
figure(2),imshow(src)