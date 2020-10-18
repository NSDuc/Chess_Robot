%clear;clc;
%src = imread('D:\nntest\testimg\test191_1.jpg');
src = im2uint8(roi4);
img = imresize(src,[90,90]);
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
r = 35;
c = [45 45];
BW = poly2mask(r*cos(t)+c(1), r*sin(t)+c(2), 90, 90);
Q = immultiply(PP,BW);
%}

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

%target = 'D:\nntest\testimg\';
%imwrite(closeQ,[target,'r17.jpg'],'quality',100);


load(fullfile('C:\','nntest','red5.mat'));
%predictedLabel = red5.classify(closeQ);

%----------------------------------------------
[label,score] = classify(red5,closeQ);
[~,idx] = sort(score,'descend');
idx = idx(5:-1:1);
classNames = red5.Layers(end).ClassNames;
classNamesTop = classNames(idx);
scoreTop = score(idx);
figure(3),barh(scoreTop)
xlim([0 1])
title({char(label),num2str(max(score),2)});
xlabel('Probability')
yticklabels(classNamesTop)
YAxisLocation = 'right';
%}
%---------------------------------------------
figure(2),imshow(closeQ);
%title(char(predictedLabel))