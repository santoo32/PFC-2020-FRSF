from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import video_demo as vd


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
    
    def clicked(self):
        vd.startDetection()

    def initUI(self):
        # self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Orwell Surveillance")
        
        self.setObjectName("Dialog")
        self.resize(655, 500)
        
        self.runButton = QtWidgets.QDialogButtonBox(self)
        self.runButton.setGeometry(QtCore.QRect(20, 60, 341, 32))
        self.runButton.setOrientation(QtCore.Qt.Horizontal)
        self.runButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.runButton.setObjectName("runButton")
        self.runButton.clicked.connect(self.clicked)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 0, 101, 51))
        self.label.setTabletTracking(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label.setText("PFC - 2020 - V0.1")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 421, 351))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./img/unnamed.png"))
        self.label_2.setObjectName("label_2")        
        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("my first label!")
        # self.label.move(50,50)

        # self.b1 = QtWidgets.QPushButton(self)
        # self.b1.setText("click me!")
        # self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()