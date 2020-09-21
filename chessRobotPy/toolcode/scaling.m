clear; clc;

for k = 2201:2380
str1='D:\nntest\chess\red\ØX\'; str3='.jpg';
str2 = num2str(k);
SC = [str1, str2, str3];
src = imread(SC);
img=imresize(src,[90,90]);
ss = 'D:\nntest\chess\red\90ØX\';
imwrite(img, [ss, num2str(k), '.jpg'], 'quality', 100);

end

%{
gray2 = im2double(gray);
w2 = fspecial('sobel'); % sobel / prewitt
w3 = fliplr(w2');
w4 = w2';
w5 = flipud(w2);
g2 = imfilter(gray2,w2,'replicate');
g3 = imfilter(gray2,w3,'replicate');
g4 = imfilter(gray2,w4,'replicate');
g5 = imfilter(gray2,w5,'replicate');

size = size(img);
sobx = zeros(size);
sobn = zeros(size);
sobx = max(max(max(g2,g3),g4),g5);
sobn = min(min(min(g2,g3),g4),g5);
figure(3), imshow(sobx);
filsobn = gray2 - sobn;
figure(4), imshow(filsobn);
%figure(5), imshow(sobx);
%figure(6), imshow(sobx);

if (max_rb > max_gb && max_rb > 40)
    gray2 = im2double(gray);
    w = fspecial('sobel');
    edge = imfilter(gray2,w,'replicate');
    fil = gray2 - edge;
    medfil = medfilt2(fil);
    imwrite(medfil,['beidentified.jpg'],'quality',80);
    identify_img = imread('beidentified.jpg');
    load(fullfile('D:\','nntest','red2.mat'));
    predictedLabel = red2.classify(identify_img);
    %clear 
elseif (max_gb > max_rb && max_gb > 40)
    predictedLabel = 'back';
else
    gray2 = im2double(gray);
    w = fspecial('sobel');
    edge = imfilter(gray2,w,'replicate');
    fil = gray2 - edge;
    medfil = medfilt2(fil);
    imwrite(medfil,['beidentified.jpg'],'quality',80);
    identify_img = imread('beidentified.jpg');
    load(fullfile('D:\','nntest','black2.mat'));
    predictedLabel = black2.classify(identify_img);
end

%}
%{
to = linspace(0, 2*pi, 50);
ro = 85;
co = [90 90];
BWo = poly2mask(ro*cos(to)+co(1), ro*sin(to)+co(2), 180, 180);
ti = linspace(0, 2*pi, 50);
ri = 70;
ci = [90 90];
BWi = poly2mask(ri*cos(ti)+ci(1), ri*sin(ti)+ci(2), 180, 180);
cir = BWo - BWi;
se = translate(strel(1),[0 0]);
mcc = imdilate(cir,se);
mcc(mcc == -Inf) = 0;
cc = mcc .* bw2;
%}