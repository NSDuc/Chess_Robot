# Generated with SMOP  0.41
from libsmop import *
# .\TrainFromScratch.m

    clear
    clc
    ## Load and Explore the Image Data
    digitDatasetPath=fullfile('C:\','aaa')
# .\TrainFromScratch.m:3
    digitData=imageDatastore(digitDatasetPath,'IncludeSubfolders',true,'LabelSource','foldernames')
# .\TrainFromScratch.m:4
    ## Check the number of images in each category.
    CountLabel=digitData.countEachLabel
# .\TrainFromScratch.m:8
    ## Specify Training and Test Sets
    trainingNumFiles=675
# .\TrainFromScratch.m:11
    rng(1)
    trainDigitData,testDigitData=splitEachLabel(digitData,trainingNumFiles,'randomize',nargout=2)
# .\TrainFromScratch.m:13
    ## Change the network architecture
    
    layers=concat([imageInputLayer(concat([90,90,1])),convolution2dLayer(3,16,'Padding',1),batchNormalizationLayer,reluLayer,maxPooling2dLayer(2,'Stride',2),convolution2dLayer(3,16,'Padding',1),batchNormalizationLayer,reluLayer,maxPooling2dLayer(2,'Stride',2),convolution2dLayer(3,32,'Padding',1),batchNormalizationLayer,reluLayer,fullyConnectedLayer(2),softmaxLayer,classificationLayer])
# .\TrainFromScratch.m:18
    # Specify training options
    options=trainingOptions('sgdm','MaxEpochs',10,'MiniBatchSize',128,'InitialLearnRate',0.0001,'ExecutionEnvironment','cpu','Plots','training-progress','ValidationData',testDigitData,'ValidationFrequency',30)
# .\TrainFromScratch.m:42
    # Train the network
    testtttt=trainNetwork(trainDigitData,layers,options)
# .\TrainFromScratch.m:53
    
    # Classify the Images in the Test Data and Compute Accuracy
    predictedLabels=classify(testtttt,testDigitData)
# .\TrainFromScratch.m:56
    valLabels=testDigitData.Labels
# .\TrainFromScratch.m:57
    # Calculate the accuracy.
    accuracy=sum(predictedLabels == valLabels) / numel(valLabels)
# .\TrainFromScratch.m:60
    #Save Network
    save('testtttt')