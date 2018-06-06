#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from fawen import W2

style = """
        .QPushButton{
        border-style:none;
        border:1px solid #C2CCD8; 
        color:#F0F0F0;  
        padding:5px;
        min-height:20px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);
        }
	"""


class MyForm(QtGui.QDialog):
    parentclicked = QtCore.pyqtSignal(str)   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
     
      
    
        self.label = QtGui.QLabel(u'接收子窗口数据：',self)
        self.label2 = QtGui.QLabel(u'给子窗口发送数据：',self)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit2 = QtGui.QLineEdit()
        self.button = QtGui.QPushButton(u'子窗口',self)
        self.button2 = QtGui.QPushButton(u'发送',self)
        layout = QtGui.QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(self.lineEdit,0,1)
        layout.addWidget(self.label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)
        layout.addWidget(self.button,2,0)
        layout.addWidget(self.button2,2,1)
        self.setLayout(layout)
        self.setWindowTitle(u'父窗口')

        self.button.clicked.connect(self.child)
        self.button2.clicked.connect(self.parentsend)
        qApp.setStyleSheet(style)

    def child(self):
        self.w2 = W2()
        self.w2.childclicked.connect(self.recv)
        self.parentclicked.connect(self.recv2)
        self.w2.show()

    def parentsend(self):
        str = self.lineEdit2.text()
        self.parentclicked.emit(str)
        
        
        
  
  
    def recv(self,s):
        self.lineEdit.setText(s)


    def recv2(self,s):
       
        self.w2.lineEdit2.setText(s)
     
      
 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
