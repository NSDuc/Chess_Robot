import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
import numpy as np
import variables as var
import chesslocation
import calcu_position
import ConvoNN

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

        self.selc      = np.zeros(33).T
        self.chess     = np.zeros(33).T
        self.order     = np.zeros(33).T
        self.index     = np.zeros(33).T
        self.prior     = np.zeros(33).T
        self.predicted = np.zeros(33).T

        # init global variables
        var.init()
        chesslocation.init()

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

    # Button6 startBtn
    def cb_button_start(self):
        global currentj1 
        global currentj36
        global currentj6 
        import chesslocation
        print("startBtn")

        selc      = self.selc
        chess     = self.chess
        order     = self.order
        index     = self.index
        prior     = self.prior
        predicted = self.predicted
        L = np.shape(posX)[0]
        s = self.s
        # [~,sortidx] = sortrows(order,1)
        # sortchess = index(sortidx,:);
        # var.sortchess = sortchess
        # var.sortidx   = sortidx
        for j in range(L):
            # curt_tag = sortchess[j,find(sortchess[j,:])]
            # tag_check = find(strcmp(prior[curt_tag, 9], "0"))
            # tag = curt_tag(tag_check(1))
            currentj1, currentj36 = robot_clamp2.robot_clamp2(
                                                            s,
                                                            chess[sortidx[j], 0],
                                                            chess[sortidx[j], 1],
                                                            chess[sortidx[j], 2],
                                                            chess[sortidx[j], 4],
                                                            currentj1,
                                                            currentj36
                                                            )
            if tag == 23:
                currentj1, currentj36 = robot_turn_2.robot_turn_2(
                                                                s,
                                                                currentj1,
                                                                currentj36
                                                                )
                # global frame2
                # load camera
                # handles.cam1 = webcam(1)
                # handles.cam1.Resolution = '1280x960'
                # frame2 = snapshot(handles.cam1);
                # frame2 = undistortImage(frame2,cameraParams);
                # delete(handles.cam1);
                # clear cam1;
                # Show the graph of axes5
                # axes(handles.axes5);
                # imshow(frame2);
                tx, ty = turn_catch.turn_catch(frame2);
                # turnroi = frame2(tx-50:tx+49,ty-50:ty+49,:);
                # Show grap of axes7
                # axes(handles.axes7);
                # imshow(turnroi);
                # roi = im2uint8(turnroi);
                # predictedLabel(L+1) = ConvoNN.ConvoNN(roi);
                # predicted(L+1) = string(predictedLabel(L+1));
                ## var.predicted = predicted.copy()
                # pause(0.1)
                # curt_tag = find(strcmp(predicted(L+1),prior));
                # tag_check = find(strcmp(prior(curt_tag,9),"0"));
                # tag = curt_tag(tag_check(1));
                currentj1, currentj36 =robot_turn2_2.robot_turn2_2(
                                                                s,
                                                                currentj1,
                                                                currentj36
                                                                );
                ## robo_tag[j,:] = str2double(prior(tag,4:8));
            else:
                ## robo_tag[j,:] = str2double(prior[tag,3:8])\

        # Show graph of axes 5
        # axes(handles.axes5);
        # imshow(frame2);


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