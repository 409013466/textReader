import sys
import time

from PyQt5.QtWidgets import QApplication,QWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog

from uiReader import Ui_MainWindow
from reader import play, stop, config

cfgData = {'fileName':'','readingTimes':1, 'rate':15, 'interval':5}
class ThreadClass(QtCore.QThread):
    anySignal = QtCore.pyqtSignal(name='finished')
    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)
        #self.is_running = True
    def run(self):
        while True:
            time.sleep(0.01)
    def play(self):
        config(cfgData['readingTimes'], cfgData['rate'], cfgData['interval'])
        if cfgData['fileName']:
            play(cfgData['fileName'])
            #self.thread.anySignal.connect(self.myFunc)
        self.anySignal.emit()
    def stop(self):
        stop()
        #self.is_running = False
        #self.terminate()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_ui()
        self.ui.openFile.clicked.connect(self.open_file)
        self.ui.play.clicked.connect(self.play)
        #self.ui.config.clicked.connect(self.config)
        self.ui.stop.clicked.connect(self.stop)
        #self.fileName = None
        cfgData['fileName'] = None
        self.thread=None
        print("new thread will be creat")
        self.thread = ThreadClass(parent=None)
        self.thread.start()
        self.thread.anySignal.connect(self.initialize_ui)

    def config(self):
        cfgData['readingTimes'] = int(self.ui.times.currentText())
        cfgData['rate'] = self.ui.rate.value()
        cfgData['interval'] = int(self.ui.interval.currentText())
        print('readingTimes value:', cfgData['readingTimes'])
        print('speechRate value:', cfgData['rate'])
        print('interval value:', cfgData['interval'])
        config(cfgData['readingTimes'], cfgData['rate'], cfgData['interval'])
    def stop(self):
        stop()
        self.ui.play.setEnabled(True)
        self.ui.stop.setEnabled(False)

    def play(self):
        #print("play button")
        self.ui.play.setEnabled(False)
        self.ui.stop.setEnabled(True)
        cfgData['readingTimes'] = int(self.ui.times.currentText())
        cfgData['rate'] = self.ui.rate.value()
        cfgData['interval'] = int(self.ui.interval.currentText())
        if cfgData['fileName']:
            self.thread.play()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, '打开文件', 'E:\\', '文本文件 (*.txt)')
        print('fileName:',fileName,fileName[0], type(fileName),type(fileName[0]))
        if fileName[0]:
            self.ui.fileDir.setText(fileName[0])
            self.ui.play.setEnabled(True)
            #self.fileName = fileName[0]
            cfgData['fileName'] = fileName[0]
        else:
            self.ui.fileDir.setText('请选择一个文件')
            self.ui.play.setEnabled(False)
            print('请选择一个文件')

    def initialize_ui(self):
        cfgData['readingTimes'] = int(self.ui.times.currentText())
        cfgData['rate'] = self.ui.rate.value()
        cfgData['interval'] = int(self.ui.interval.currentText())
        cfgData['fileName'] = self.ui.fileDir.toPlainText()
        if cfgData['fileName'] == '请选择一个文件':
            self.ui.play.setEnabled(False)
        else:
            self.ui.play.setEnabled(True)
        self.ui.stop.setEnabled(False)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   w = MainWindow()
   #ui = Ui_MainWindow()
   #ui.setupUi(mainWindow)
   w.setWindowTitle("朗读器")
   #w.setGeometry(500, 250, 426, 230)
   w.show()
   sys.exit(app.exec_())