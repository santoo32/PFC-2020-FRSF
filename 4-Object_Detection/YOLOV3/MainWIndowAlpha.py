from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import video_demo as vd
import popupWindow as detectionWindow
import cv2


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.dialogs = list()
        self.initUI()
    
    # Start yolov3 detection
    def start(self):
        if self.runButton.text() == "Run":
            self.runButton.setText("Stop")
            self.runButton.setStyleSheet("""color: #000000;
                                        background-color: #d4d4d4;
                                        border-width: 1px;
                                        border-color: #1e1e1e;
                                        border-style: solid;
                                        border-radius: 6;
                                        padding: 3px;
                                        font-size: 12px;
                                        padding-left: 5px;
                                        padding-right: 5px;
                                        min-width: 40px;""")
            message = vd.startDetection(self, self.spinBox.value(), self.filePath.text())
        else:
            # System exit on stop pressing because I dont know how to reinitialize all the variables
            sys.exit()
           


    def initUI(self):
        # Main window
        self.resize(1471, 877)
        
        # Main window title
        
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.title = QtWidgets.QLabel(self)
        self.title.setFont(font)
        self.title.setGeometry(QtCore.QRect(500, 10, 600, 100))
        self.title.setTabletTracking(False)
        self.title.setWordWrap(True)
        self.title.setObjectName("label")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        # Start detection button
        self.runButton = QtWidgets.QPushButton(self)
        self.runButton.setGeometry(QtCore.QRect(1310, 820, 121, 41))
        self.runButton.setIconSize(QtCore.QSize(20, 20))
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.runButton.setStyleSheet("""color: #ffffff;
                                        background-color: #006e0f;
                                        border-width: 1px;
                                        border-color: #1e1e1e;
                                        border-style: solid;
                                        border-radius: 6;
                                        padding: 3px;
                                        font-size: 12px;
                                        padding-left: 5px;
                                        padding-right: 5px;
                                        min-width: 40px;""")
        self.runButton.clicked.connect(self.start)
        
        # Separator line
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(1240, 20, 21, 841))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        # Spinner box title
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(1260, 240, 81, 16))
        self.label_2.setObjectName("label_2")
        # Confidence spinbox
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(1260, 260, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        # self.spinBox.valueChanged.connect(self.valuechange)
        
        # Big main label to display an image
        self.imageDisplay = QtWidgets.QLabel(self)
        self.imageDisplay.setGeometry(QtCore.QRect(10, 60, 1221, 801))
        self.imageDisplay.setObjectName("label_4")

        #Video file input
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(1260, 130, 81, 16))
        self.label_5.setObjectName("label_5")
        self.filePath = QtWidgets.QLineEdit(self)
        self.filePath.setGeometry(QtCore.QRect(1260, 150, 131, 20))
        self.filePath.setObjectName("lineEdit")
        self.examineButton = QtWidgets.QPushButton(self)
        self.examineButton.setGeometry(QtCore.QRect(1400, 150, 61, 20))
        self.examineButton.setObjectName("pushButton")
        self.examineButton.setText("Examine")
        self.examineButton.clicked.connect(self.getfiles)

        # Values initialization
        self.setWindowTitle("Neural Network surveillance")
        self.title.setText("PFC - 2020 - V1.1.1")
        self.runButton.setText("Run")
        self.label_2.setText("Confidence")
        self.label_5.setText("Video file")
        self.imageDisplay.setText("")

    # Get files from a path
    def getfiles(self):
      dlg = QFileDialog(self)
      # Set available file types 
      dlg.setNameFilters(["Videos (*.mp4 *.mkv)"])

		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            # Update input text field and label 
            self.filePath.setText(f.name)

    def button_clicked(self):
        dialog = detectionWindow.DetectionWindow(self)
        self.dialogs.append(dialog)
        dialog.show()

def window():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()