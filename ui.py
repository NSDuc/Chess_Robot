import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

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

        self.recognBtn.clicked.connect(lambda x: print("Reg"))
        self.recognBtn.setFixedSize(200,50)
        self.startBtn.clicked.connect(lambda x: print("startBtn"))
        self.connectBtn.clicked.connect(lambda x: print("connectBtn"))
        self.robotOnBtn.clicked.connect(lambda x: print("robotOnBtn"))
        self.stopBtn.clicked.connect(lambda x: print("stopBtn"))
        self.exitBtn.clicked.connect(lambda x: print("exitBtn"))

        layout = QVBoxLayout()
        layout.addWidget(self.recognBtn)
        layout.addWidget(self.startBtn)
        layout.addWidget(self.connectBtn)
        layout.addWidget(self.robotOnBtn)
        layout.addWidget(self.stopBtn)
        layout.addWidget(self.exitBtn)
        return layout

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()