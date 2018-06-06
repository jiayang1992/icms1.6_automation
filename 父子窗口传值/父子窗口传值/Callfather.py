# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:53:30 2018

@author: Administrator
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from father import Ui_W1
from Callchild import W2

class W1(QWidget,Ui_W1):
    parentclicked = pyqtSignal(str)   

    def __init__(self, parent=None):
        super(W1, self).__init__(parent)        
        self.setupUi(self)
        self.w2 = W2()
        self.pushButton.clicked.connect(self.child)
        self.pushButton_2.clicked.connect(self.parentsend)
        
    def child(self):
        self.w2 = W2()
        self.w2.childclicked.connect(self.recv)
        self.parentclicked.connect(self.recv2)
        self.w2.show()

    def parentsend(self):
        str = self.lineEdit_2.text()
        self.parentclicked.emit(str)
        
        
        
  
  
    def recv(self,s):
        self.lineEdit.setText(s)


    def recv2(self,s):
       
        self.w2.lineEdit_2.setText(s)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = W1()
    ui.show()
    sys.exit(app.exec_())
