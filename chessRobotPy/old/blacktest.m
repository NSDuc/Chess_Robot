clear;clc;
src = imread('D:\nntest\testimg\b\test72.jpg');
img = imresize(src,[180,180]);
gray = rgb2gray(img);

radrange = 90;
%tic;
[accum, circen, cirrad] = CircularHough_Grd(gray, [radrange * 0.78, radrange]);
%toc;
maxvalue = max(accum(:));
[x, y] = find(accum == maxvalue);

level=graythresh(gray);
bw = im2bw(gray,level);
se = strel('disk',2);
openbw = imopen(bw,se);
bw2 = imcomplement(openbw);

mask = ones(size(gray)) .* bw2;
mask = uint8(mask);
PP = gray .* mask;

t = linspace(0, 2*pi, 50);
r = 70;
c = [90 90];
BW = poly2mask(r*cos(t)+c(1), r*sin(t)+c(2), 180, 180);
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

se = translate(strel(1),[0 0]); %[up_down left_right]
moveQ = imdilate(closeQ,se);


load(fullfile('D:\','nntest','black.mat'));
predictedLabel = black.classify(moveQ);

%----------------------------------------------
[label,score] = classify(black,moveQ);
[~,idx] = sort(score,'descend');
idx = idx(5:-1:1);
classNames = black.Layers(end).ClassNames;
classNamesTop = classNames(idx);
scoreTop = score(idx);
figure(1),barh(scoreTop)
xlim([0 1])
title({char(label),num2str(max(score),2)});
xlabel('Probability')
yticklabels(classNamesTop)
YAxisLocation = 'right';
%---------------------------------------------
%figure(2),imshow(moveQ);
%title(char(predictedLabel))
%}
%figure(3),imshow(bw2);
figure(4),imshow(closeQ);