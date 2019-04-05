from PyQt5.QtWidgets import QWidget,QVBoxLayout,QScrollArea
from PyQt5.QtCore import Qt
from win32api import GetSystemMetrics as GSM

import PyQt5


lst = [u"D", u"E", u"EF", u"F", u"FG", u"G", u"H", u"JS", u"J", u"K", u"M", u"P", u"R", u"S", u"T", u"U", u"V", u"X", u"Y", u"Z"]

class App(QWidget):
    config={
        'top':10,
        'left':10,
        'width':GSM(0)/2,
        'height':GSM(0)/2
        }


    def __init__(self):
         super().__init__(parent=None)
         self.initUI()
         
         self.createLayout_Container()
         self.layout_All = QVBoxLayout(self)
         self.layout_All.addWidget(self.scrollarea)

    def initUI(self):
        self.setGeometry(self.config['top'],self.config['left'],self.config['width'],self.config['height'])
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(.7)
        self.setAutoFillBackground(True)  
        self.setStyleSheet("background:red;")


    def createLayout_Container(self):
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedWidth(self.config['width'])
        self.scrollarea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollarea.setWidget(widget)
        self.layout_SArea = QVBoxLayout(widget)
        self.layout_SArea.addStretch(1)

    def add(self,layout):
        self.layout_SArea.setContentsMargins(0,0,0,0)
        self.layout_SArea.addLayout(layout)
        
