clear;clc;
%% Load and Explore the Image Data
digitDatasetPath = fullfile('C:\','aaa');
digitData = imageDatastore(digitDatasetPath, ...
    'IncludeSubfolders', true, 'LabelSource', 'foldernames');

%% Check the number of images in each category.
CountLabel = digitData.countEachLabel

%% Specify Training and Test Sets
trainingNumFiles = 675;
rng(1) % For reproducibility
[trainDigitData,testDigitData] = splitEachLabel(digitData, ...
    trainingNumFiles, 'randomize');

%% Change the network architecture

layers = [
    imageInputLayer([90 90 1])
    
    convolution2dLayer(3,16,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,16,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,32,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    fullyConnectedLayer(2)
    softmaxLayer
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
testtttt = trainNetwork(trainDigitData, layers, options); % convnet2

% Classify the Images in the Test Data and Compute Accuracy
predictedLabels  = classify(testtttt, testDigitData); 
valLabels  = testDigitData.Labels;

% Calculate the accuracy.
accuracy = sum(predictedLabels == valLabels)/numel(valLabels)

%Save Network
save testtttt
