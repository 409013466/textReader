import sys
from PyQt5.QtWidgets import QApplication,QWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog

from uiReader import Ui_MainWindow
from reader import play, stop, config

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_ui()
        self.ui.openFile.clicked.connect(self.open_file)
        self.ui.play.clicked.connect(self.play)
        self.ui.config.clicked.connect(self.config)
        self.ui.stop.clicked.connect(self.stop)
        self.fileName = None
        self.readingTimes = 1
        self.speechRate = 15
        self.interval = 3

    def config(self):
        self.readingTimes = int(self.ui.times.currentText())
        self.speechRate = self.ui.rate.value()
        self.interval = int(self.ui.interval.currentText())
        print('self.readingTimes value:', self.readingTimes)
        print('self.speechRate value:', self.speechRate)
        print('self.interval value:', self.interval)
        config(self.readingTimes, self.speechRate, self.interval)
    def stop(self):
        stop()
    def play(self):
        self.config()
        if self.fileName:
            play(self.fileName)

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, '打开文件', 'E:\\', '文本文件 (*.txt)')
        print('fileName:',fileName,fileName[0], type(fileName),type(fileName[0]))
        if fileName[0]:
            self.ui.fileDir.setText(fileName[0])
            self.fileName = fileName[0]
        else:
            self.ui.fileDir.setText('请选择一个文件')
            print('请选择一个文件')

    def initialize_ui(self):
        self.readingTimes = int(self.ui.times.currentText())
        self.speechRate = self.ui.rate.value()
        self.interval = int(self.ui.interval.currentText())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   w = MainWindow()
   #ui = Ui_MainWindow()
   #ui.setupUi(mainWindow)
   w.setWindowTitle("朗读器")
   #w.setGeometry(500, 250, 426, 230)
   w.show()
   sys.exit(app.exec_())