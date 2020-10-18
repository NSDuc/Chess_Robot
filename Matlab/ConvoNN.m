
function predictedLabel = ConvoNN(roi)
%function gray = ConvoNN(roi)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
%load(fullfile('D:\','nntest','red3.mat'));
%load(fullfile('D:\','nntest','red4.mat'));
load(fullfile('red5.mat'));
load(fullfile('black2.mat'));
img = imresize(roi,[90,90]);
gray = rgb2gray(img);
r = img(:,:,1); g = img(:,:,2); b = img(:,:,3);
gb = g - b;
rb = r - b;
median_gb = median(median(gb)); median_rb = median(median(rb));
%assignin('base','median_gb',median_gb);
assignin('base','median_rb',median_rb);
if (median_rb > median_gb && median_rb >= 5)
    Q = redpreprocess(gray);
    predictedLabel = red5.classify(Q);
    % predictedLabel = testtttt.classify(Q);
    %predictedLabel = red3.classify(Q);
    if predictedLabel == 'r¨®'||predictedLabel == '¥K'||predictedLabel == '¬¶'%
            predictedLabel = red4.classify(Q);%
    end
elseif (median_gb > median_rb && median_gb >= 15)
   Q = imcomplement(im2bw(gray,0.38));
    predictedLabel = categorical(cellstr('­I­±'));
else
   Q = blackpreprocess(gray);
    predictedLabel = black2.classify(Q);
end
assignin('base','predictedLabel',predictedLabel);

end

