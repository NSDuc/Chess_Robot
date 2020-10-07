import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore  import *
from PyQt5.QtGui   import *
import numpy as np
import cv2
import calcu_position

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

    self.setWindowTitle("Chess Robot")
    self.setGeometry(100, 100, 1000, 500)

    layoutMain = QVBoxLayout()
    layoutImgs = QHBoxLayout()
    layoutChss = QHBoxLayout()
    layoutBtns = self.getLayoutButtons()

    layoutMain.addLayout(layoutImgs)
    layoutMain.addLayout(layoutChss)

    self.label1 = QLabel("LABEL 1")
    self.label2 = QLabel("LABEL 2")
    self.label3 = QLabel("LABEL 3")
    self.label1.setAlignment(Qt.AlignCenter)
    self.label2.setAlignment(Qt.AlignCenter)
    self.label3.setAlignment(Qt.AlignCenter)


    self.tableWidget = QTableWidget(32, 3)
    self.tableWidget.setFixedSize(500, 250)
    tab1vbox = QVBoxLayout()
    tab1vbox.setContentsMargins(5, 5, 5, 5)
    tab1vbox.addWidget(self.tableWidget)

    layoutImgs.addWidget(self.label1)
    layoutImgs.addWidget(self.label2)
    layoutImgs.addWidget(self.label3)

    layoutChss.addLayout(tab1vbox)
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

  # Button1
  def cb_button_recognition(self):
    print("recBtn")
    self.src = cv2.imread(r'E:\robot_arm\matlab_only\img100.jpg')
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
    _     , bw = cv2.threshold (recognition, thresh*0.72, 255, cv2.THRESH_BINARY)
    
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

    posX = np.array(posX_list).T
    posY = np.array(posY_list).T

    roi_list = []
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
      roi_list.append(closeQ)

    roi = roi_list[0]
    qformat = QImage.Format_Indexed8
    img = QImage(roi,
                 roi.shape[1],
                 roi.shape[0],
                 roi.strides[0],
                 qformat)
    img = img.rgbSwapped()
    self.label3.setPixmap(QPixmap.fromImage(img))
    self.label3.setAlignment(Qt.AlignCenter)

    # TODO ConVoNN
    predicted_all = np.array(["仕","車","相","傌","炮","兵","炮","相","兵","兵","帥","兵","兵","炮","仕","傌"])
    predicted = predicted_all[0:len(chess_list)].copy()
    
    chessdata = np.array([predicted.T, posX, posY])
    posi      = np.array([posX, posY])
    m, n = chessdata.shape
    
    self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
    self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
    self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
    self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
    self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
    self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
    self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
    self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))

    for i in range(len(chess_list)):
      self.tableWidget.setItem(i,0, QTableWidgetItem(predicted[i]))
      self.tableWidget.setItem(i,1, QTableWidgetItem(str(posX[i])))
      self.tableWidget.setItem(i,2, QTableWidgetItem(str(posY[i])))
    chess, order, index, prior = calcu_position.calcu_position(predicted, posX, posY)

  # Button6 startBtn
  def cb_button_start(self):
    print("startBtn")

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