import sys
import serial
import numpy as np
import cv2
from keras.models import load_model

from PyQt5.QtWidgets import *
from PyQt5.QtCore  import *
from PyQt5.QtGui   import *

import calcu_position
import catchroi
import ConvoNN
import robot_arm

import os
import time, threading
import re

import test_param

com_robot  = 'COM1'
com_matlab = 'COM3'
no_camera  = True
first_read = True
test_param.init()

position_regex = re.compile(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)')
robot_arm.init_sequence()

matlab_serial          = serial.Serial()
matlab_serial.port     = com_matlab
matlab_serial.baudrate = 9600
matlab_serial.bytesize = 8
matlab_serial.parity   = 'N'
matlab_serial.stopbits = 1

robot_serial          = serial.Serial()
robot_serial.port     = com_robot
robot_serial.baudrate = 9600
robot_serial.bytesize = 8
robot_serial.parity   = 'N'
# robot_serial.stopbits = 1

def read_robot_position():
  global position_regex
  global robot_serial
  global matlab_serial
  global first_read

  if first_read == True:
    first_read = False
    threading.Timer(1, read_robot_position).start()
    return

  print(time.ctime())

  if matlab_serial.is_open == False:
    try:
      matlab_serial.open()
      print("Connected to matlab")
    except:
      print("Not connect to matlab")
      threading.Timer(1, read_robot_position).start()
      return

  if robot_serial.is_open == False:
    print("Not connect to robot")
  else:
    print("Waiting data from robot...")
    robot_arm.writeSerial(robot_serial, matlab_serial, '@READ')
    line = robot_arm.readSerial(robot_serial)
    ## Sample to test on Hercules: 1,2,-294.0,0,0,-294.0,0#010#013
    print(line)
    match = position_regex.search(line)
    if match == None:
      print("Not match format")
    else:
      robot_arm.writeSerial(matlab_serial, line)

  threading.Timer(1, read_robot_position).start()
  return

class Color(QWidget):
  def __init__(self, color, *args, **kwargs):
    super(Color, self).__init__(*args, **kwargs)
    self.setAutoFillBackground(True)
    
    palette = self.palette()
    palette.setColor(QPalette.Window, QColor(color))
    self.setPalette(palette)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.model_red = load_model(r'model_red.h5')
    self.model_red2 = load_model(r'model_red2.h5')
    self.model_black = load_model(r'model_black.h5')
    self.model_red.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    self.model_red2.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    self.model_black.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    self.reset_variable()

    self.setWindowTitle("Chess Robot")
    self.setGeometry(100, 100, 1000, 500)

    layoutMain = QVBoxLayout()
    layoutImgs = QHBoxLayout()
    layoutChss = QHBoxLayout()
    layoutBtns = self.getLayoutButtons()

    layoutMain.addLayout(layoutImgs)
    layoutMain.addLayout(layoutChss)

    self.label1 = QLabel("Captured Image")
    self.label2 = QLabel("Binary Image")
    self.label3 = QLabel("Captured Chess")
    self.label4 = QLabel("Binary Chess")
    self.label1.setAlignment(Qt.AlignCenter)
    self.label2.setAlignment(Qt.AlignCenter)
    self.label3.setAlignment(Qt.AlignCenter)
    self.label4.setAlignment(Qt.AlignCenter)

    self.textbox = QLineEdit()

    self.tableWidget = QTableWidget(32, 3)
    self.tableWidget.setFixedSize(500, 250)
    tab1vbox = QVBoxLayout()
    tab1vbox.setContentsMargins(50, 5, 5, 5)
    tab1vbox.addWidget(self.tableWidget)

    tableHHeader0 = QTableWidgetItem()
    tableHHeader1 = QTableWidgetItem()
    tableHHeader2 = QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(0, tableHHeader0)
    self.tableWidget.setHorizontalHeaderItem(1, tableHHeader1)
    self.tableWidget.setHorizontalHeaderItem(2, tableHHeader2)
    self.tableWidget.horizontalHeaderItem(0).setText("Predicted")
    self.tableWidget.horizontalHeaderItem(1).setText("PositionX")
    self.tableWidget.horizontalHeaderItem(2).setText("PositionY")
    self.tableWidget.clicked.connect (self.cb_table)

    chessvbox = QVBoxLayout()
    chessvbox.addWidget(self.label3)
    chessvbox.addWidget(self.label4)
    chessvbox.addWidget(self.textbox)

    layoutImgs.addWidget(self.label1)
    layoutImgs.addWidget(self.label2)

    layoutChss.addLayout(tab1vbox)
    layoutChss.addLayout(chessvbox)
    layoutChss.addLayout(layoutBtns)

    widget = QWidget()
    widget.setLayout(layoutMain)
    self.setCentralWidget(widget)

  def getLayoutButtons(self):
    self.recognBtn  = QPushButton("Recognition")
    self.startBtn   = QPushButton("Start")
    self.connectBtn = QPushButton("Connect")
    self.robotOnBtn = QPushButton("Robot On")
    self.stopBtn = QPushButton("Stop")
    self.exitBtn = QPushButton("Exit")


    self.recognBtn.setFixedSize(100,25)
    self.startBtn.setFixedSize(100,25)
    self.connectBtn.setFixedSize(100,25)
    self.robotOnBtn.setFixedSize(100,25)
    self.stopBtn.setFixedSize(100,25)
    self.exitBtn.setFixedSize(100,25)

    self.connectBtn.setCheckable(True)
    self.robotOnBtn.setCheckable(True)
    self.stopBtn.setCheckable(True)

    self.recognBtn.clicked.connect (self.cb_button_recognition)
    self.startBtn.clicked.connect  (self.cb_button_start)
    self.connectBtn.clicked.connect(self.cb_button_connect)
    self.robotOnBtn.clicked.connect(self.cb_button_robot)
    self.stopBtn.clicked.connect   (self.cb_button_stop)
    self.exitBtn.clicked.connect   (self.cb_button_exit)

    layout = QVBoxLayout()
    layout.addWidget(self.recognBtn)
    layout.addWidget(self.startBtn)
    layout.addWidget(self.connectBtn)
    layout.addWidget(self.robotOnBtn)
    layout.addWidget(self.stopBtn)
    layout.addWidget(self.exitBtn)
    return layout

  def reset_variable(self):
    self.raw_chess_list = []
    self.chess_list = []
    self.chess     = None
    self.order     = None
    self.index     = None
    self.prior     = None
    self.predicted = None

    self.currentj1  = 0
    self.currentj36 = 0
    self.currentj6  = 0

  def cb_table(self, item):
    if item.row() >= len(self.raw_chess_list):
      return

    raw_chess = self.raw_chess_list[item.row()]
    qformat = QImage.Format_RGB888
    img = QImage(raw_chess,
                 raw_chess.shape[1],
                 raw_chess.shape[0],
                 raw_chess.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label3.setPixmap(QPixmap.fromImage(img))
    self.label3.setAlignment(Qt.AlignCenter)

    chess = self.chess_list[item.row()]
    qformat = QImage.Format_Indexed8
    img = QImage(chess,
                 chess.shape[1],
                 chess.shape[0],
                 chess.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label4.setPixmap(QPixmap.fromImage(img))
    self.label4.setAlignment(Qt.AlignCenter)

  def reset_table(self):
    for i in range(len(self.chess_list)):
      self.tableWidget.setItem(i,0, QTableWidgetItem(""))
      self.tableWidget.setItem(i,1, QTableWidgetItem(""))
      self.tableWidget.setItem(i,2, QTableWidgetItem(""))

  # Button1
  def cb_button_recognition(self):
    self.reset_table()
    self.reset_variable()

    if test_param.import_picture: #apply
      picname = r"D:\Project\ChessRobot\nntest\testimg\Picture " +self.textbox.text()+ ".jpg"
      print(picname)
      if os.path.exists(picname) == False:
        return
      self.setWindowTitle(picname)
      src_img = cv2.imread(picname)
    else: #apply
      src_img = self.captureFrame()

    self.textbox.setText("")
    qformat = QImage.Format_RGB888
    img = QImage(src_img,
                 src_img.shape[1],
                 src_img.shape[0],
                 src_img.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label1.setPixmap(QPixmap.fromImage(img).scaledToWidth(360))
    self.label1.setAlignment(Qt.AlignCenter)

    openbw, self.raw_chess_list, posX, posY = catchroi.catchroi (src_img)
    qformat = QImage.Format_Indexed8
    img = QImage(openbw,
                 openbw.shape[1],
                 openbw.shape[0],
                 openbw.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label2.setPixmap(QPixmap.fromImage(img).scaledToWidth(360))
    self.label2.setAlignment(Qt.AlignCenter)

    print('Number of chess: '+ str(len(self.raw_chess_list)))

    label_list = []
    for raw_chess in self.raw_chess_list:
      label, bw_chess = ConvoNN.ConvoNN (raw_chess, self.model_red, self.model_red2, self.model_black)
      label_list.append (label)
      self.chess_list.append (bw_chess)

    self.predicted = np.array(label_list).T

    for i in range(len(self.chess_list)):
      self.tableWidget.setItem(i,0, QTableWidgetItem(self.predicted[i]))
      self.tableWidget.setItem(i,1, QTableWidgetItem(str(posX[i])))
      self.tableWidget.setItem(i,2, QTableWidgetItem(str(posY[i])))
    self.chess, self.order, self.index, self.prior = calcu_position.calculate(self.predicted, posX, posY)

  # Button6 startBtn
  def cb_button_start(self):
    global robot_serial

    print("startBtn")
    chess     = self.chess
    order     = self.order
    index     = self.index
    prior     = self.prior
    predicted = self.predicted
    currentj1  = self.currentj1
    currentj36 = self.currentj36
    currentj6  = self.currentj6

    # selc = np.array([6,8,10,11,22,30,34,42,48,51,52,54,62,64,65,72])
    # posX = np.array([409,435,460,472,512,553,584,618,645,660,720,730,788,808,823,847]).T
    # posY = np.array([555,662,457,353,548,655,428,542,332,674,420,565,677,339,470,594]).T
    # predicted = np.array(["仕","r車","相","傌","炮","兵","炮","相","兵","兵","帥","兵","兵","炮","仕","傌"])
    # predicted = np.array(["rGuard","rChariot","rElephant","rHorse","rCannon","rSoldier","rCannon","rElephant","rSoldier","rSoldier","rGeneral","rSoldier","rSoldier","rCannon","rGuard","rHorse"])
    # chess, order, index, prior = robot_arm.calcu_position(predicted, posX, posY)
    L         = predicted.shape[0]
    prior     = np.c_[prior, np.zeros((prior.shape[0],1), dtype=np.int)]
    robo_tag  = np.zeros((L,5), dtype=np.int)
    sortidx   = np.argsort(order[:, 0])
    sortchess = order[np.argsort(order[:, 0])]
    print(chess)
    print(order)
    print(index)
    print(prior)
    print(predicted)
    print(L)
    print(sortidx)
    print(sortchess)
    for j in range(L):
      print("j =", j)

      # curt_tag  = sortchess[j,np.argwhere(sortchess[j,:]>=0)]
      # tag_check = np.where(prior[curt_tag,8] == '0')[0]
      # print("tag_check=", tag_check)
      # tag = curt_tag[tag_check[0]]

      sortchess_column = np.nonzero(sortchess[j,:])
      tag = int(sortchess[j,0])
      for column in sortchess_column[0]:
        tag = int(sortchess[j,column])
        if prior[tag,8] == '0':
          break
      print("tag=", tag)

      self.currentj1, self.currentj36 = robot_arm.robot_clamp2(robot_serial, matlab_serial,
        chess[sortidx[j],0], chess[sortidx[j],1],chess[sortidx[j],2],chess[sortidx[j],4], self.currentj1, self.currentj36)
      if tag == 23: #[tag == 22 ???]
        frame2 = self.captureFrame()
        tx, ty  = catchroi.turn_catch(frame2)
        turnroi = frame2[tx-50:tx+49,ty-50:ty+49,:]
        roi     = turnroi.astype(np.uint8)
        label, bw_chess = ConvoNN.ConvoNN(roi, self.model_red, self.model_red2, self.model_black)

        self.predicted = np.append(self.predicted, [label]) #self.predicted[L] = label
        
        self.tableWidget.setItem(L,0, QTableWidgetItem(self.predicted[L]))
        self.tableWidget.setItem(L,1, QTableWidgetItem(str(tx)))
        self.tableWidget.setItem(L,2, QTableWidgetItem(str(ty)))
        robot_arm.pause(0.1)

        curt_tag  = np.where(self.predicted[L+1] == prior)
        tag_check = np.where(prior[curt_tag,8] == '0')[0]
        tag = curt_tag[tag_check[0]]
        self.currentj1, self.currentj36 = robot_arm.robot_turn2_2(robot_serial, matlab_serial,
          self.currentj1, self.currentj36);
        robo_tag[j,:] = prior[tag,3:8].astype(np.int)
      else:
        robo_tag[j,:] = prior[tag,3:8].astype(np.int)

      self.currentj1, self.currentj36, check = robot_arm.robot_place2(robot_serial, matlab_serial,
        robo_tag[j,0], robo_tag[j,1], robo_tag[j,2], robo_tag[j,3], robo_tag[j,4], self.currentj1, self.currentj36)
      prior[tag,8] = check

  # Button2
  def cb_button_connect(self):
    global robot_serial
    global matlab_serial

    print("connectBtn")
    if self.connectBtn.isChecked():
      try:
        robot_serial.open()
        print("Connected to robot")
        self.connectBtn.setText("Disconnect")
        # read_robot_position()
      except:
        print("Cannot connect to robot")
        self.connectBtn.setChecked(False)
        sys.exit(0)
      try:
        matlab_serial.open()
        print("Connected to matlab")
      except:
        print("Cannot connect to matlab")
        sys.exit(0)
    else:
       robot_serial.close()
       matlab_serial.close()
       print("Disconnect")
       self.connectBtn.setText("Connect")

  # Button7
  def cb_button_robot(self):
    global robot_serial

    print("robotOnBtn")
    if self.robotOnBtn.isChecked():
      print("Robot on")
      robot_arm.writeSerial(robot_serial, matlab_serial, '@STEP 221, 0, 0, 0, 0, 0, 430', 2)
      self.currentj6 = 430
      self.robotOnBtn.setText("Robot off")
    else:
      print("Robot off")
      robot_arm.writeSerial(robot_serial, matlab_serial, '@STEP 221, 0, 0, 0, 0, 0, -430', 2)
      currentj6 = 0
      self.robotOnBtn.setText("Robot on")

  # Button4
  def cb_button_stop(self):
    print("stopBtn")
    if self.stopBtn.isChecked():
       print("Stop")
       # Stop the whole program to wait for user pressing button again
       self.stopBtn.setText("Continue")
    else:
       print("Continue")
       self.stopBtn.setText("Stop")


  # Button5
  def cb_button_exit(self):
    global robot_serial
    global matlab_serial

    print("exitBtn")
    robot_serial.close()
    matlab_serial.close()
    self.close()
    sys.exit(0)
    # Disconnect from serial

  def captureFrame(self): #apply
    cam = cv2.VideoCapture(0)
    cam.set(3,1280)
    cam.set(4,960)
    _, frame = cam.read()
    return frame

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()