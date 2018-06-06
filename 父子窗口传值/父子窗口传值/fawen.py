#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidegts import *
 
 
 
 
 
 
class W2(QtGui.QDialog):
 
    childclicked = QtCore.pyqtSignal(str)   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
      
        self.label = QtGui.QLabel(u'给父窗口发送数据：')
        self.label2 = QtGui.QLabel(u'接收父窗口数据：')
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit2 = QtGui.QLineEdit()
        self.button = QtGui.QPushButton(u'发送',self)
        layout = QtGui.QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(self.lineEdit,0,1)
        layout.addWidget(self.label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)
        layout.addWidget(self.button,2,0,1,2)
        self.setLayout(layout)
        self.setWindowTitle(u'子窗口')
 
 
        self.button.clicked.connect(self.childsend)

    
 
 
    def childsend(self):
        str = self.lineEdit.text()
        self.childclicked.emit(str)
 
  
   
  
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = W2()
    myapp.show()
    sys.exit(app.exec_())
