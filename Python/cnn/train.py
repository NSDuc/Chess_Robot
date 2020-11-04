import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

import cv2
import numpy as np

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Sequential(         # input shape (1, 90, 90)
            nn.Conv2d(
                in_channels=1,              # input height
                out_channels=16,            # n_filters
                kernel_size=3,              # filter size
                stride=1,                   # filter movement/step
                padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
            ),                              # output shape (16, 90, 90)
            nn.ReLU(),                      # activation
            nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 45, 45)
        )
        self.conv2 = nn.Sequential(         # input shape (16, 45, 45)
            nn.Conv2d(16, 32, 3, 1, 1),     # output shape (32, 45, 45)
            nn.ReLU(),                      # activation
            nn.MaxPool2d(2),                # output shape (32, 23, 23)
        )
        self.out = nn.Linear(
            in_features=(32 *23 *23),
            out_features=7
        )   # fully connected layer, output 7 classes

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        output = self.out(x)
        return output, x           # return x for visualization

class Net2(nn.Module):
    def __init__(self):
        super(Net2, self).__init__()

        self.conv1 = nn.Sequential(         # input shape (1, 90, 90)
            nn.Conv2d(
                in_channels=1,              # input height
                out_channels=16,            # n_filters
                kernel_size=3,              # filter size
                stride=1,                   # filter movement/step
                padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
            ),                              # output shape (16, 90, 90)
            nn.BatchNorm2d(16),
            nn.ReLU(),                      # activation
            nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 45, 45)
        )
        self.conv2 = nn.Sequential(         # input shape (16, 45, 45)
            nn.Conv2d(16, 32, 3, 1, 1),     # output shape (32, 45, 45)
            nn.BatchNorm2d(32),
            nn.ReLU(),                      # activation
            nn.MaxPool2d(2),                # output shape (32, 23, 23)
        )
        self.out = nn.Linear(
            in_features=(32 *23 *23),
            out_features=7
        )   # fully connected layer, output 7 classes

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        output = self.out(x)
        return output, x           # return x for visualization


TRAN_TO_TENSOR = transforms.ToTensor()
LABEL_MAPS = ["Cannon", "Chariot", "Elephant", "General", "Guard", "Horse", "Soldier"]

def load_cnn(path):
    model = Net()
    model.load_state_dict(torch.load(path))
    return model
def load_cnn2(path):
    model = Net2()
    model.load_state_dict(torch.load(path))
    return model

def predict(model, cvimage):
    ptimage = TRAN_TO_TENSOR(cvimage).unsqueeze(0)

    outputs, auxq = model(ptimage)
    _, predicted = torch.max(outputs, 1)
    return LABEL_MAPS[predicted]

if __name__ == '__main__':

    TRAIN = True # True False
    TEST  = True # True False

    COLOR       = "black" # red black
    MODEL_CLASS = "Net2" # Net2 Net

    
    if COLOR == "red":
        MODEL_PATH = 'redA.pth'
        TEST_SIZE = 18
        EPOCH = 10
    else: 
        MODEL_PATH = 'blackA.pth'
        TEST_SIZE = 17
        EPOCH = 10

    DATA_PATH = "data_" + COLOR
    TEST_PATH = "data_" + COLOR + "_test/"
	
    if TRAIN:

        trainset = torchvision.datasets.ImageFolder(
            root = DATA_PATH, #đường dẫn tới thư mục chứa ảnh để training
            transform = transforms.Compose(
                        [transforms.Grayscale(num_output_channels=1),
                         transforms.Resize([90,90]),
                         transforms.ToTensor()]) #giai đoạn tiền xử lý ảnh để training: gồm đọc ảnh dạng Gray ==> resize thành 90x90 ==> chuyển thành kiểu dữ liệu Tensor
        )

        trainloader = torch.utils.data.DataLoader(
            trainset,
            batch_size=128,
            num_workers=2, #dùng nhiều thread để đọc ảnh, ko cần quan tâm
            shuffle=True #random ảnh cho quá trình training
        ) #mô tả cách lấy dữ liệu training để mạng CNN học

        #load mạng CNN từ Net/Net2 Class
        if MODEL_CLASS == "Net":
            net = Net()
        else:
            net = Net2()

        #Định nghĩa phương pháp tính sai số, tối ưu, learning ...
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

        for epoch in range(EPOCH):  # loop over the dataset multiple times
            running_loss = 0.0
            print("epoch =", epoch)
            for i, data in enumerate(trainloader, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                outputs, _  = net(inputs) #tính toán "dự đoán" output ứng với dữ liệu inputs
                loss = criterion(outputs, labels) #tính toán loss
                loss.backward()
                optimizer.step()

                # print statistics
                running_loss += loss.item()
                print(i)

        torch.save(net.state_dict(), MODEL_PATH) #lưu model train đc vào file
        del net

    if TEST:
        if MODEL_CLASS == "Net":
            net = Net()
        else:
            net = Net2()
        net.load_state_dict(torch.load(MODEL_PATH))

        for i in range(1,TEST_SIZE+1):
            path = TEST_PATH + str(i) + '.jpg'
            cvimage = cv2.imread(path, 0)
            cvimage = cv2.resize(cvimage, (90,90))

            print("predict", i, ": ", predict(net, cvimage))

            cv2.imshow(path, cvimage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()






