import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

currentj1  = 0
currentj36 = 0
currentj6  = 0

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

        self.setWindowTitle("My Awesome App")

        layoutMain = QVBoxLayout()
        layoutImgs = QHBoxLayout()
        layoutCtrl = QHBoxLayout()
        layoutBtns = self.getLayoutButtons()

        layoutMain.addLayout(layoutImgs)
        layoutMain.addLayout(layoutCtrl)

        label1 = QLabel("LABEL 1")
        label2 = QLabel("LABEL 2")
        label3 = QLabel("LABEL 3")
        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)

        layoutImgs.addWidget(label1)
        layoutImgs.addWidget(label2)
        layoutImgs.addWidget(label3)
        
        layoutCtrl.addWidget(Color("Blue"))
        layoutCtrl.addWidget(Color("Yellow"))

        layoutCtrl.addLayout(layoutBtns)

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


        self.recognBtn.setFixedSize(200,50)

        self.connectBtn.setCheckable(True)
        #self.connectBtn.toggle()
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
        # 1. Capture image to variable frame1 and show to variable axes1
        # 2. Run catchroi(frame): 
        #    openbw : black white image to axes3
        #    undistort image
        #    posX, posY: position of all roi on the table
        #    regionXb = c(selc,1);
        #    regionXe = c(selc,1) + c(selc,3);
        #    regionYb = c(selc,2);
        #    regionYe = c(selc,2) + c(selc,4);
        #    #roi1=src(regionYb(1):regionYe(1),regionXb(1):regionXe(1))
        #    #assignin('base','roi1',roi1);
        #    #roi = im2uint8(roi1);
        #    #roi = im2uint8(roi2);
        #    #roi = im2uint8(roi3);
        #    #roi = im2uint8(roi4);
        #  3. Show roi4 to axe5
        print("recBtn")

    # Button6
    def cb_button_start(self):
        global currentj1 
        global currentj36
        global currentj6 
        print("startBtn")

    # Button2
    def cb_button_connect(self):
        print("connectBtn")
        # TODO: Connect to serial
        if self.connectBtn.isChecked():
           print("Connect")
           self.connectBtn.setText("Disconnect")
        else:
           print("Disconnect")
           self.connectBtn.setText("Connect")

    # Button7
    def cb_button_robot(self):
        print("robotOnBtn")
        if self.robotOnBtn.isChecked():
           print("Robot on")
           self.robotOnBtn.setText("Robot off")
        else:
           print("Robot off")
           self.robotOnBtn.setText("Robot on")

    # Button4
    def cb_button_stop(self):
        print("stopBtn")
        if self.stopBtn.isChecked():
           print("Stop")
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