clear;clc;
%% Load and Explore the Image Data
digitDatasetPath = fullfile(matlabroot,'toolbox','nnet','nndemos', ...
    'nndatasets','DigitDataset');
digitData = imageDatastore(digitDatasetPath, ...
    'IncludeSubfolders', true, 'LabelSource', 'foldernames');

%% Check the number of images in each category.
CountLabel = digitData.countEachLabel

%% Specify Training and Test Sets
trainingNumFiles = 750;
rng(1) % For reproducibility
[trainDigitData,testDigitData] = splitEachLabel(digitData, ...
    trainingNumFiles, 'randomize');

%% Define the Network Layers
% Define the convolutional neural network architecture.

layers = [
    imageInputLayer([28 28 1])
    convolution2dLayer(5, 20)
    reluLayer
    maxPooling2dLayer(2, 'Stride', 2)
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];

%% Add network validation during training
%% Specify the Training Options
options = trainingOptions(...
    'sgdm',...
    'MaxEpochs', 10, ...
    'MiniBatchSize', 128,...
    'InitialLearnRate', 0.0001,...
    'ExecutionEnvironment', 'cpu',...
    'Plots', 'training-progress',...
    'ValidationData', testDigitData,...
    'ValidationFrequency', 30);

%% Train the Network Using Training Data
convnet = trainNetwork(trainDigitData, layers, options);

%% Change the network architecture

layers = [
    imageInputLayer([28 28 1])
    
    convolution2dLayer(3,16,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,32,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,64,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];

% Specify training options
options = trainingOptions(...
    'sgdm',...
    'MaxEpochs', 5, ...
    'MiniBatchSize', 128,...
    'InitialLearnRate', 0.01,...
    'ExecutionEnvironment', 'cpu',... 
    'Plots', 'training-progress',...
    'ValidationData', testDigitData,...
    'ValidationFrequency', 30);

% Train the network
convnet2 = trainNetwork(trainDigitData, layers, options);

% Classify the Images in the Test Data and Compute Accuracy
predictedLabels  = classify(convnet2, testDigitData);
valLabels  = testDigitData.Labels;

% Calculate the accuracy.
accuracy = sum(predictedLabels == valLabels)/numel(valLabels)

%% Try to classify something else
img = imread('letterW.png');
actualLabel = 'W';

predictedLabel = convnet2.classify(img);

figure, imshow(img);
title(['Predicted: ' char(predictedLabel) ', Actual: ' char(actualLabel)])