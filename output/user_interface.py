import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore  import *
from PyQt5.QtGui   import *
import numpy as np
import cv2
import calcu_position
from keras.models import load_model

import robot_arm

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

    self.chess_label = ['Cannon', 'Chariot', 'Elephant', 'General', 'Guard', 'Horse', 'Sodier']

    self.model_red = load_model('model_red.h5')
    self.model_black = load_model('model_black.h5')

    self.roi_list = []
    self.chess     = None
    self.order     = None
    self.index     = None
    self.prior     = None
    self.predicted = None

    self.currentj1  = 0
    self.currentj36 = 0
    self.currentj6  = 0

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
    self.label3 = QLabel("Chess")
    self.label1.setAlignment(Qt.AlignCenter)
    self.label2.setAlignment(Qt.AlignCenter)
    self.label3.setAlignment(Qt.AlignCenter)


    self.tableWidget = QTableWidget(32, 3)
    self.tableWidget.setFixedSize(500, 180)
    tab1vbox = QVBoxLayout()
    tab1vbox.setContentsMargins(5, 5, 5, 5)
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

    layoutImgs.addWidget(self.label1)
    layoutImgs.addWidget(self.label2)

    layoutChss.addLayout(tab1vbox)
    layoutChss.addWidget(self.label3)
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

  def cb_table(self, item):
    print("You clicked on row " + str(item.row()) + " column " + str(item.column()))
    roi = self.roi_list[item.row()]
    qformat = QImage.Format_Indexed8
    img = QImage(roi,
                 roi.shape[1],
                 roi.shape[0],
                 roi.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label3.setPixmap(QPixmap.fromImage(img))
    self.label3.setAlignment(Qt.AlignCenter)

  # Button1
  def cb_button_recognition(self):
    print("recBtn")
    self.src = cv2.imread('Picture1.jpg')
    gray_src = cv2.cvtColor(self.src, cv2.COLOR_BGR2GRAY)
    qformat = QImage.Format_RGB888
    img = QImage(self.src,
                 self.src.shape[1],
                 self.src.shape[0],
                 self.src.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label1.setPixmap(QPixmap.fromImage(img).scaledToWidth(360))
    self.label1.setAlignment(Qt.AlignCenter)

    b,g,r = cv2.split(self.src)
    recognition = (0.1*r + 0.1*g + 0.8*b).astype(np.uint8)
    thresh, a  = cv2.threshold(recognition, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    _     , bw = cv2.threshold (recognition, thresh*0.4, 255, cv2.THRESH_BINARY)
    
    bw = 255 - bw
    se = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]], np.uint8)
    
    openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)
    qformat = QImage.Format_Indexed8
    img = QImage(openbw,
                 openbw.shape[1],
                 openbw.shape[0],
                 openbw.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label2.setPixmap(QPixmap.fromImage(img).scaledToWidth(360))
    self.label2.setAlignment(Qt.AlignCenter)
    
    contours, hierarchy = cv2.findContours(openbw,  
        cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    chess_list = []
    posX_list  = []
    posY_list  = []
    for con in contours:
        rect = cv2.boundingRect(con)
        if rect[2] > 70 and rect[3] > 70:
            regionXb = rect[0]
            regionXe = rect[0] + rect[2]
            regionYb = rect[1]
            regionYe = rect[1] + rect[3]
            posX_list.append(int(rect[0] + rect[2] / 2))
            posY_list.append(int(rect[1] + rect[3] / 2))
            sub_image = openbw[regionYb:regionYe,regionXb:regionXe]
            chess_list.append(gray_src[regionYb:regionYe,regionXb:regionXe].copy())
    
    print('Number of chess: '+ str(len(chess_list)))
    print(posX_list)
    print(posY_list)
    posX = np.array(posX_list).T
    posY = np.array(posY_list).T
    
    # Mark Position on image
    blue_dot = [255,0,0]
    for i in range(len(posX_list)):
      self.src[(posY_list[i] - 2):(posY_list[i] + 2),(posX_list[i] - 2):(posX_list[i] + 2)] = blue_dot
    cv2.imwrite("dot.jpg",self.src)
    
    for index in range(len(chess_list)):
      gray = cv2.resize(chess_list[index], dsize=(90, 90), interpolation=cv2.INTER_LINEAR)
      thresh, a = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
      _ , bw = cv2.threshold (gray, thresh*0.72, 255, cv2.THRESH_BINARY)
      bw = 255 - bw
    
      se = np.array([[0,0,1,0,0],
                     [0,1,1,1,0],
                     [1,1,1,1,1],
                     [0,1,1,1,0],
                     [0,0,1,0,0]], np.uint8)
      openbw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, se)
    
      mask = np.ones(gray.shape) * openbw
      mask = mask / 255
      mask = mask.astype(np.uint8)
    
      PP = gray * mask
    
      BW_circle = np.zeros((90, 90))
      BW_circle = cv2.circle(BW_circle, (45, 45), 35, (255, 255, 255), -1)
      BW_circle = BW_circle / 255
      BW = BW_circle.astype(np.uint8).copy()
      Q = PP * BW

      unique_elements, counts_elements = np.unique(Q.flatten(), return_counts=True)
      unique_elements = np.delete(unique_elements, [0])
      counts_elements = np.delete(counts_elements, [0])
      totalpercent = np.sum(counts_elements)
      l = unique_elements.size
      percent = 0
      for i in range(0,l):
          percent = percent + counts_elements[i]
          if float(percent) > (float(totalpercent)*0.66):
              break
      th=unique_elements[i]
    
      Q[Q > th] = 0
      Q[Q > 0]  = 255
    
      closeQ = cv2.morphologyEx(Q, cv2.MORPH_CLOSE, se)
      cv2.imwrite("roi" + str(index) + ".jpg", closeQ)
      self.roi_list.append(closeQ)

    label_list = []
    for i in range(len(chess_list)):
      X = np.reshape(self.roi_list[i],[1,90,90,1])
      label_index = self.model_red.predict_classes(X)[0]
      label_list.append(self.chess_label[label_index])
    self.predicted = np.array(label_list).T

    chessdata = np.array([self.predicted.T, posX, posY])
    print(chessdata)
    posi      = np.array([posX, posY])
    print(chessdata.shape)
    m, n = chessdata.shape

    for i in range(len(chess_list)):
      self.tableWidget.setItem(i,0, QTableWidgetItem(self.predicted[i]))
      self.tableWidget.setItem(i,1, QTableWidgetItem(str(posX[i])))
      self.tableWidget.setItem(i,2, QTableWidgetItem(str(posY[i])))
    self.chess, self.order, self.index, self.prior = calcu_position.calcu_position(self.predicted, posX, posY)

  # Button6 startBtn
  def cb_button_start(self):
    print("startBtn")
    # chess     = self.chess
    # order     = self.order
    # index     = self.index
    # prior     = self.prior
    # predicted = self.predicted
    # s         = self.s
    currentj1   = self.currentj1
    currentj36  = self.currentj36
    currentj6   = self.currentj6
    
    selc = np.array([6,8,10,11,22,30,34,42,48,51,52,54,62,64,65,72])
    posX = np.array([409,435,460,472,512,553,584,618,645,660,720,730,788,808,823,847]).T
    posY = np.array([555,662,457,353,548,655,428,542,332,674,420,565,677,339,470,594]).T
    predicted = np.array(["仕","r車","相","傌","炮","兵","炮","相","兵","兵","帥","兵","兵","炮","仕","傌"])
    chess, order, index, prior = robot_arm.calcu_position(predicted, posX, posY)

    L         = selc.shape[0]
    prior     = np.c_[prior, np.zeros((prior.shape[0],1))]
    robo_tag  = np.zeros((L,5))
    sortidx   = np.argsort(order[:, 0])
    sortchess = order[np.argsort(order[:, 0])]

    for j in range(L):
      print("j =", j)
      curt_tag  = sortchess[j,np.nonzero(sortchess[j,:])[0]]
      tag_check = np.where(prior[curt_tag.astype(np.int),8] == '0')[0]
      tag       = curt_tag[tag_check[0]]

      currentj1, currentj36 = robot_arm.robot_clamp2(chess[sortidx[j],0], chess[sortidx[j],1],chess[sortidx[j],2],chess[sortidx[j],4], currentj1, currentj36)
      if tag == 23:
        cam = cv2.VideoCapture(0)
        _ , frame2 = cam.read()

        tx, ty  = turn_catch(frame2)
        turnroi = frame2[tx-50:tx+49,ty-50:ty+49,:]
        roi     = turnroi.astype(np.unit8)
        predictedLabel[L+1] = ConvoNN(roi)
        predicted[L+1]      = str(predictedLabel[L+1])
        robot_arm.pause(0.1)
      else:
        robo_tag[j,:] = prior[int(tag),3:8].astype(np.int);

      currentj1, currentj36, check = robot_arm.robot_place2(robo_tag[j,0], robo_tag[j,1], robo_tag[j,2], robo_tag[j,3], robo_tag[j,4], currentj1, currentj36)
      prior[int(tag),8] = check
    
  # Button2
  def cb_button_connect(self):
    print("connectBtn")
    if self.connectBtn.isChecked():
      print("Connect")
      self.s = serial.Serial('COM1', 9600, bytesize=8, parity='N', stopbits=1)
      self.connectBtn.setText("Disconnect")
    else:
       print("Disconnect")
       self.connectBtn.setText("Connect")

  # Button7
  def cb_button_robot(self):
    print("robotOnBtn")
    if self.robotOnBtn.isChecked():
      print("Robot on")
      self.s.write('@STEP 221,0,0,0,0,0,430,0')
      self.currentj6 = 430
      self.robotOnBtn.setText("Robot off")
    else:
      print("Robot off")
      self.s.write('@STEP 221,0,0,0,0,0,-430,0')
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
    print("exitBtn")
    # Disconnect from serial

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()