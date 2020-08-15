from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import video_demo as vd


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
    
    # Start yolov3 detection
    def start(self):
        message = vd.startDetection(self, self.spinBox.value(), self.filePath.text())
        # print(message)

    def valuechange(self):
        print(self.spinBox.value())

    def initUI(self):
        # Main window
        self.resize(926, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_34913.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        # Main window title
        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(350, 0, 141, 51))
        self.title.setTabletTracking(False)
        self.title.setWordWrap(True)
        self.title.setObjectName("label")
        
        # Start detection button
        self.runButton = QtWidgets.QPushButton(self)
        self.runButton.setGeometry(QtCore.QRect(750, 550, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Downloads/identidad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon1)
        self.runButton.setIconSize(QtCore.QSize(20, 20))
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.runButton.clicked.connect(self.start)
        
        # Separator line
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(700, 30, 21, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        # Spinner box title
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(720, 230, 81, 16))
        self.label_2.setObjectName("label_2")
        # Confidence spinbox
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(720, 250, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.valuechange)
        
        # Big main label to display an image
        self.imageDisplay = QtWidgets.QLabel(self)
        self.imageDisplay.setGeometry(QtCore.QRect(10, 60, 661, 521))
        self.imageDisplay.setObjectName("label_4")

        #Video file input
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(720, 100, 81, 16))
        self.label_5.setObjectName("label_5")
        self.filePath = QtWidgets.QLineEdit(self)
        self.filePath.setGeometry(QtCore.QRect(720, 120, 131, 20))
        self.filePath.setObjectName("lineEdit")
        self.examineButton = QtWidgets.QPushButton(self)
        self.examineButton.setGeometry(QtCore.QRect(860, 120, 61, 20))
        self.examineButton.setObjectName("pushButton")
        self.examineButton.setText("Examine")
        self.examineButton.clicked.connect(self.getfiles)

        # Values initialization
        self.setWindowTitle("Orwell surveillance")
        self.title.setText("PFC - 2020 - V0.2")
        self.runButton.setText("Run")
        self.label_2.setText("Confidence")
        self.label_5.setText("Video file")
        self.imageDisplay.setText("")

        
        # Custom color palete, currently unused

        # dark_palette = QtGui.QPalette()

        # dark_palette.setColor(QPalette.Window, QColor(235, 235, 235))
        # dark_palette.setColor(QPalette.WindowText, QColor(235, 235, 235))
        # dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        # dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        # dark_palette.setColor(QPalette.ToolTipBase, QColor('white'))
        # dark_palette.setColor(QPalette.ToolTipText, QColor('white'))
        # dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        # dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        # dark_palette.setColor(QPalette.ButtonText, QColor('white'))
        # dark_palette.setColor(QPalette.BrightText, QColor('red'))
        # dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        # dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # dark_palette.setColor(QPalette.HighlightedText, QColor('black'))

        # self.setPalette(dark_palette)

        # self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

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

    
def window():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()