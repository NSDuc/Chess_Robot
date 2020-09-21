load(fullfile('D:\','nntest','red.mat'));
clearvars -except red;
%clear;clc;

%% Load and Explore the Image Data
digitDatasetPath = fullfile('D:\','nntest','chess','redmove_r','new');
digitData = imageDatastore(digitDatasetPath, ...
    'IncludeSubfolders', true, 'LabelSource', 'foldernames');

%% Check the number of images in each category.
CountLabel = digitData.countEachLabel
net = red;
layersTransfer = net.Layers(1:end-1);
%% Specify Training and Test Sets
trainingNumFiles = 675;
rng(1) % For reproducibility
[trainDigitData,testDigitData] = splitEachLabel(digitData, ...
    trainingNumFiles, 'randomize');

%% Change the network architecture

layers = [
    layersTransfer
    %fullyConnectedLayer(7)
    %softmaxLayer
    classificationLayer];

% Specify training options
options = trainingOptions(...
    'sgdm',...
    'MaxEpochs', 10, ...
    'MiniBatchSize', 128,...
    'InitialLearnRate', 0.0001,...
    'ExecutionEnvironment', 'cpu',... 
    'Plots', 'training-progress',...
    'ValidationData', testDigitData,...
    'ValidationFrequency', 30);

% Train the network
red3 = trainNetwork(trainDigitData, layers, options); % convnet2

% Classify the Images in the Test Data and Compute Accuracy
predictedLabels  = classify(red3, testDigitData); 
valLabels  = testDigitData.Labels;

% Calculate the accuracy.
accuracy = sum(predictedLabels == valLabels)/numel(valLabels)

%Save Network
save red3
%}