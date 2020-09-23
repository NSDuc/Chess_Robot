#nsduc: pip install pyserial
import serial

#%clear;clc%clear parament clc commad
#%clearvars -except s; clc;
def init():
    global s
    s = serial.Serial('COM1')

init()
# if exist('s') == 0
#     s = serial('COM1','BaudRate',9600,'DataBits', 8,'Terminator','CR');
#     fopen(s);
