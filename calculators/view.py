# http://srinikom.github.io/pyside-docs/PySide/QtGui/QGridLayout.html#PySide.QtGui.PySide.QtGui.QGridLayout.addLayout
# http://zetcode.com/gui/qt4/layoutmanagement/
# Import statements:

import sys

from traits.api import Int, Float
from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication
#from pyface.qt import QString

# The class to be edited with the TableEditor:
class Application ():
    compute_box = 0.0 
    temp = 0.0
    count = 0
    dot = -1

    app = QApplication(sys.argv)
    window = QWidget()
    textEdit = QTextEdit()
    textEdit.setReadOnly(True)
    textEdit.setText(unicode(compute_box))

    nine_button = QPushButton('9')
    eight_button = QPushButton('8')
    seven_button = QPushButton('7')
    six_button = QPushButton('6')
    five_button = QPushButton('5')
    four_button = QPushButton('4')
    three_button = QPushButton('3')
    two_button = QPushButton('2')
    one_button = QPushButton('1')

    equals_button = QPushButton('=')
    add_button = QPushButton('+')
    subtract_button = QPushButton('-')
    mul_button = QPushButton('*')
    div_button = QPushButton('/')
    zero_button = QPushButton('0')
    dot_button = QPushButton('.')

    clr_button = QPushButton('clr')

    def nine_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +9.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +9.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def eight_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +8.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +8.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def seven_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +7.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +7.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def six_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +6.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +6.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def five_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +5.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +5.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def four_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +4.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +4.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def three_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +3.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +3.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def two_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +2.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +2.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def one_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +1.0
            self.textEdit.setText(unicode(self.compute_box))
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +1.0)/10**(self.dot)
            self.dot +=1
            self.textEdit.setText(unicode(self.compute_box))

    def zero_button_fired(self):
        # does some weird shit!
        if self.dot == -1: 
            self.compute_box = self.compute_box*10
            self.textEdit.setText(unicode(self.compute_box))
#        else:
            # dunno what to do when we want to add 
            # after zero!

    def dot_button_fired(self):
            self.dot = 1

    def eval_expr(self):
        if self.count == 1:
            self.compute_box += self.temp
        elif self.count == -1:
            self.compute_box = self.temp -self.compute_box
        elif self.count == 2:
            self.compute_box = self.compute_box*self.temp
        elif self.count == -2:
            self.compute_box = self.temp/self.compute_box
        self.dot = -1
        self.count = 0
        self.textEdit.setText(unicode(self.compute_box))
        self.temp = 0.0
    
    def add_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 1
        self.dot = -1
        self.textEdit.setText(unicode(self.compute_box))

    def subtract_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -1
        self.dot = -1
        self.textEdit.setText(unicode(self.compute_box))

    def mul_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 2
        self.dot = -1
        self.textEdit.setText(unicode(self.compute_box))

    def div_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -2
        self.dot = -1
        self.textEdit.setText(unicode(self.compute_box))

    def clr_button_fired(self):
        self.temp = 0.0
        self.compute_box = 0.0
        self.count = 0
        self.dot =-1 
        self.textEdit.setText(unicode(self.compute_box))

    def layout(self):
        self.nine_button.clicked.connect(self.nine_button_fired)
        self.eight_button.clicked.connect(self.eight_button_fired)
        self.seven_button.clicked.connect(self.seven_button_fired)
        self.six_button.clicked.connect(self.six_button_fired)
        self.five_button.clicked.connect(self.five_button_fired)
        self.four_button.clicked.connect(self.four_button_fired)
        self.three_button.clicked.connect(self.three_button_fired)
        self.two_button.clicked.connect(self.two_button_fired)
        self.one_button.clicked.connect(self.one_button_fired)
        self.zero_button.clicked.connect(self.zero_button_fired)

        self.mul_button.clicked.connect(self.mul_button_fired)
        self.add_button.clicked.connect(self.add_button_fired)
        self.subtract_button.clicked.connect(self.subtract_button_fired)
        self.div_button.clicked.connect(self.div_button_fired)
        self.dot_button.clicked.connect(self.dot_button_fired)
        self.clr_button.clicked.connect(self.clr_button_fired) 
        self.equals_button.clicked.connect(self.eval_expr)

        textlayout = QGridLayout()
        layout = QGridLayout()
        #layout.addWidget(window,3,3)
        mainlayout = QVBoxLayout()
	textlayout.addWidget(self.textEdit)
	layout.addWidget(self.one_button,1,1)
	layout.addWidget(self.two_button,1,2)
	layout.addWidget(self.three_button,1,3)
        layout.addWidget(self.four_button,2,1)
        layout.addWidget(self.five_button,2,2)
        layout.addWidget(self.six_button,2,3)
	layout.addWidget(self.seven_button,3,1)
        layout.addWidget(self.eight_button,3,2)
        layout.addWidget(self.nine_button,3,3)
        layout.addWidget(self.zero_button,4,2)

	layout.addWidget(self.mul_button,4,1)
        layout.addWidget(self.add_button,5,1)
        layout.addWidget(self.div_button,4,3)
        layout.addWidget(self.dot_button,5,2)
	layout.addWidget(self.subtract_button,5,3)
        layout.addWidget(self.clr_button,6,1)
        layout.addWidget(self.equals_button,6,3)

        mainlayout.addLayout(textlayout)
        mainlayout.addLayout(layout)
	self.window.setLayout(mainlayout)
        self.window.setWindowTitle("Calculator : Poruri Sai Rahul")

    def main(self):
        self.layout()
	self.window.show()

	return self.app.exec_()

# Create the demo:
demo = Application()

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.main()
