import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


clear;clc;
%% Load and Explore the Image Data
digitDatasetPath = fullfile('C:\\','aaa');
digitData = imageDatastore(digitDatasetPath, ...
    'IncludeSubfolders', true, 'LabelSource', 'foldernames');

%% Check the number of images in each category.
CountLabel = digitData.countEachLabel

%% Specify Training and Test Sets
trainingNumFiles = 675;
rng(1) % For reproducibility
np.random.seed(1)

[trainDigitData,testDigitData] = splitEachLabel(digitData, ...
    trainingNumFiles, 'randomize');

%% Change the network architecture
model = keras.Sequential (
    keras.Input(shape=(90, 90, 1)),
    layers.Conv2D(filters=16, kernel_size=3, padding='valid'),
    layers.BatchNormalization(),
    layers.ReLU(),

    layers.MaxPooling2D(pool_size=(2, 2), strides=(3,3)),
    layers.Conv2D(filters=16, kernel_size=3, padding='valid'),
    layers.BatchNormalization(),
    layers.ReLU(),
    
    layers.MaxPooling2D(pool_size=(2, 2), strides=(3,3)),
    layers.Conv2D(filters=32, kernel_size=3, padding='valid'),
    layers.BatchNormalization(),
    layers.ReLU(),
    
    layers.Dense(units=2),
    layers.Softmax(),
    layers.Dense(),
)

model.compile(
    loss='categorical_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
    )
   
model.fit()

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
