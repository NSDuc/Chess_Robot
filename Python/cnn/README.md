=========================================================================================================

pip install torch

=========================================================================================================

download and extract folders at this path:
- data_black
- data_red
- data_red_2

by the following link: https://drive.google.com/file/d/1n_gPAV0gY6PvGjQn0RryLm9SqZD7LV0B/view?usp=sharing

=========================================================================================================

red.pth  : train with data_red + 10 epoch
red0.pth : train with data_red_2 + 10 epoch
red1.pth : train with data_red + 20 epoch
red2.pth : train with data_red_2 + 20 epoch


black.pth  : train with data_black + 10 epoch
black1.pth : train with data_black + 20 epoch

=========================================================================================================
Hướng dẫn chạy file train.py:


MODEL_CLASS: mạng cnn được sử dụng (Net hoặc Net2), Net2 ok hơn.
COLOR: red/black màu của con cờ dùng trong chương trình

TRAIN = TRUE/FALSE: chương trình sẽ (không) training và tạo model để dự đoán
TEST  = TRUE/FALSE: chương trình sẽ (không) test dựa trêm model lưu trong biến MODEL_PATH

Ví dụ:
MODEL_CLASS = "Net2"
COLOR = "black"
TRAIN = True
	MODEL_PATH = "b.pth"
	EPOCH = 10
TEST = True

sẽ training mạng CNN với:
- Model sử dụng class Net2
- color là black nên sử dụng thư mục ./data_black để train và ./data_black_test để test

- TRAIN = True : chạy chương trình training với EPOCH = 10 và lưu vào file "b.pth"
- TEST = True: chạy chương trình test với một số ảnh