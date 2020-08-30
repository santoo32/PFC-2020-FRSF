from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import core.utils as utils



class DetectionWindow(QMainWindow):

    def __init__(self, parent=None):
        super(DetectionWindow,self).__init__(parent)
        self.image = QtGui.QPixmap()
        self.initUI()
    
    def setImage(self, image):
        self.image = utils.convert_cv_qt(image)
        self.imageLabel.setPixmap(QtGui.QPixmap(self.image))

    def initUI(self):
        # Dialog.setObjectName("Dialog")
        self.resize(755, 585)
        # self.setModal(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(330, 10, 81, 33))
       
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : red")
        self.imageLabel = QtWidgets.QLabel(self)
        self.imageLabel.setGeometry(QtCore.QRect(10, 100, 741, 371))
        self.imageLabel.setObjectName("imageLabel")
        

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 396, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yesButton = QtWidgets.QPushButton(self)
        self.yesButton.setGeometry(QtCore.QRect(220, 510, 321, 31))
        self.yesButton.setObjectName("yesButton")
        self.yesButton.setStyleSheet("background-color : red") 
        self.yesButton.clicked.connect(self.prompAlarm)

        self.noButton = QtWidgets.QPushButton(self)
        self.noButton.setGeometry(QtCore.QRect(340, 550, 75, 23))
        self.noButton.setObjectName("noButton")
        self.noButton.clicked.connect(self.closeWindow)

        self.setWindowTitle("Warning")
        self.label.setText("Alerta")
        self.label_2.setText("Por favor indique si en la siguiente imagen hay un arma")
        self.yesButton.setText("SI")
        self.noButton.setText("NO")

    def prompAlarm(self):
        print("Alarm")
        self.close()
    
    
    def closeWindow(self):
        self.close()


def detectionWindow():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = DetectionWindow()
    win.show()
    sys.exit(app.exec_())

# detectionWindow()