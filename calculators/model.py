# http://srinikom.github.io/pyside-docs/PySide/QtGui/QGridLayout.html#PySide.QtGui.PySide.QtGui.QGridLayout.addLayout
# http://zetcode.com/gui/qt4/layoutmanagement/

import sys

from traits.api import Int, Float
from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication
#from pyface.qt import QString

class Application ():
    compute_box = 0.0       # used to store live user input
    temp = 0.0              # used to store the previous result/entry
    count = 0               # used to check which arithmatic operation
                            # to perform among the 4!
    dot = -1                # used to keep track of where  we are
                            # adding integers, before or after the
                            # decimal point

    def eval_expr(self):
        if self.count == 1:
            self.compute_box += self.temp
        elif self.count == -1:
            self.compute_box = self.temp -self.compute_box
        elif self.count == 2:
            self.compute_box = self.compute_box*self.temp
        elif self.count == -2:
            self.compute_box = self.temp//self.compute_box
        self.dot = -1
        self.count = 0
        self.temp = 0.0

    def add_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 1
        self.dot = -1

    def subtract_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -1
        self.dot = -1

    def mul_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 2
        self.dot = -1

    def div_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -2
        self.dot = -1

    def clr_button_fired(self):
        self.temp = 0.0
        self.compute_box = 0.0
        self.count = 0
        self.dot =-1 
