%{
clear;clc;

%load('region.mat','cifar10Net');
load region.mat;

x=red.Layers(1:end-3);

lastlayers = [
fullyConnectedLayer(2,'Name','fc8','WeightLearnRateFactor',1, 'BiasLearnRateFactor',1)
softmaxLayer('Name','softmax')
classificationLayer('Name','classification')
];

mylayers=[x;lastlayers];

options =      trainingOptions('sgdm', ...
     'MiniBatchSize', 10, ...
     'InitialLearnRate', 1e-6, ...
     'MaxEpochs', 50);


myRCNN = trainRCNNObjectDetector(gTruth, mylayers, options, ...
 'NegativeOverlapRange', [0 0.3], ...
        'PositiveOverlapRange', [0.6 1]);
%}

tic;
detectedImg = imread('Picture 133.jpg');

[bbox, score, label] = detect(myRCNN, detectedImg, 'MiniBatchSize', 10);

%?¥Ü³Ì????ªG
% [score, idx] = max(score);

idx=find(score>0.3);
bbox = bbox(idx, :);

% annotation = sprintf('%s: (Confidence = %f)', label(idx(1)), score(idx(1)));
% detectedImg = insertObjectAnnotation(img, 'rectangle', bbox(1,:), annotation);

n=size(idx,1);
for i=1:n
    annotation = sprintf('%s: (Confidence = %f)', label(idx(i)), score(idx(i)));
    detectedImg = insertObjectAnnotation(detectedImg, 'rectangle', bbox(i,:), annotation);
end

figure
imshow(detectedImg);
toc;
%}