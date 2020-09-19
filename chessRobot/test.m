clear;clc
num = 2;
str1 = 'C:\nntest\testimg\test\test'; str3 = '_1'; str4 = '.jpg';
str2 = num2str(num);
src0 = imread([str1 str2 str3 str4]);
src1 = im2double(src0);
src = im2uint8(src1);
img = imresize(src,[90,90]);

gray = rgb2gray(img);
r = img(:,:,1); g = img(:,:,2); b = img(:,:,3);
gb = g - b;
rb = r - b;
max_gb = max(max(gb)); max_rb = max(max(rb));

if (max_rb > max_gb && max_rb > 40)
    x = 'red';
    Q = redpreprocess(gray);
    load(fullfile('C:\','nntest','red5.mat'));
    predictedLabel = red5.classify(Q);
elseif (max_gb > max_rb && max_gb > 40)
    x = 'back'; 
    predictedLabel = 'back';
else
    x = 'black';
    Q = blackpreprocess(gray);
    load(fullfile('C:\','nntest','black2.mat'));
    predictedLabel = black2.classify(Q);
end
figure(1), imshow(Q);
title(char(predictedLabel))