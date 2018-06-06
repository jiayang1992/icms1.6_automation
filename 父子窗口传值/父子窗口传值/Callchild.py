# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:58:29 2018

@author: Administrator
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from child import Ui_W2

class W2(QWidget,Ui_W2):
    childclicked = pyqtSignal(str)  

    def __init__(self, parent=None):
        super(W2, self).__init__(parent)        
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.childsend)
    
    def childsend(self):
        str = self.lineEdit.text()
        self.childclicked.emit(str)
        
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = W2()
    ui.show()
    sys.exit(app.exec_())