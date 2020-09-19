%clear;clc
%num = 2;
%str1 = 'D:\nntest\testimg\test'; str3 = '_1'; str4 = '.jpg';
%str2 = num2str(num);
%src = imread([str1 str2 str3 str4]);
%load(fullfile('D:\','nntest','red3.mat'));
load(fullfile('C:\','nntest','red5.mat'));
load(fullfile('C:\','nntest','black2.mat'));
%for i=1:size(selc)
for i=1
    eval(['cim = im2uint8(roi',num2str(i),');'])
    %cim = imnoise(cim,'salt & pepper',0.02);
    img = imresize(cim,[90,90]);
    
    gray = rgb2gray(img);
    r = img(:,:,1); g = img(:,:,2); b = img(:,:,3);
    gb = g - b;
    rb = r - b;
    median_gb = median(median(gb)); median_rb = median(median(rb));
    
    if (median_rb > median_gb && median_rb >= 10)
        Q = redpreprocess(gray);
        predictedLabel(i) = red5.classify(Q);
        %if predictedLabel(i) == 'r¨®'||predictedLabel(i) == '¥K'||predictedLabel(i) == '¬¶'
        %    predictedLabel(i) = red4.classify(Q);
        %end
    elseif (median_gb > median_rb && median_gb > 15)
        Q = imcomplement(im2bw(gray,0.38));
        predictedLabel(i) = categorical(cellstr('­I­±'));
    else
        Q = blackpreprocess(gray);
        predictedLabel(i) = black2.classify(Q);
        %predictedLabel(i) = categorical(cellstr('¶Â'));
    end
%end

figure(i), imshow(Q);
title(char(predictedLabel(i)))
end