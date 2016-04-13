"""
http://srinikom.github.io/pyside-docs/PySide/QtGui/QGridLayout.html#PySide.QtGui.PySide.QtGui.QGridLayout.addLayout
http://zetcode.com/gui/qt4/layoutmanagement/
"""
import sys

from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication

from newModel import Application as calcApp

# The class to be edited with the TableEditor:
class Application ():

    test = calcApp()

    def _create_buttons(self):
        
        self.nine_button = QPushButton('9')
        self.eight_button = QPushButton('8')
        self.seven_button = QPushButton('7')
        self.six_button = QPushButton('6')
        self.five_button = QPushButton('5')
        self.four_button = QPushButton('4')
        self.three_button = QPushButton('3')
        self.two_button = QPushButton('2')
        self.one_button = QPushButton('1')

        self.equals_button = QPushButton('=')
        self.add_button = QPushButton('+')
        self.subtract_button = QPushButton('-')
        self.mul_button = QPushButton('*')
        self.div_button = QPushButton('/')
        self.zero_button = QPushButton('0')
        self.dot_button = QPushButton('.')

        self.clr_button = QPushButton('clr')

    def _attach_buttons_to_actions(self):

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
        self.equals_button.clicked.connect(self.equals_button_fired)

    def nine_button_fired(self):
        self.test.push_to_stack(int(self.nine_button.text()))

    def eight_button_fired(self):
        self.test.push_to_stack(int(self.eight_button.text()))

    def seven_button_fired(self):
        self.test.push_to_stack(int(self.seven_button.text()))

    def six_button_fired(self):
        self.test.push_to_stack(int(self.six_button.text()))

    def five_button_fired(self):
        self.test.push_to_stack(int(self.five_button.text()))

    def four_button_fired(self):
        self.test.push_to_stack(int(self.four_button.text()))

    def three_button_fired(self):
        self.test.push_to_stack(int(self.three_button.text()))

    def two_button_fired(self):
        self.test.push_to_stack(int(self.two_button.text()))

    def one_button_fired(self):
        self.test.push_to_stack(int(self.one_button.text()))

    def zero_button_fired(self):
        self.test.push_to_stack(int(self.zero_button.text()))

    def dot_button_fired(self):
        self.test.push_to_stack(self.dot_button.text())

    def add_button_fired(self):
        self.test.push_to_stack(self.add_button.text())

    def subtract_button_fired(self):
        self.test.push_to_stack(self.subtract_button.text())

    def mul_button_fired(self):
        self.test.push_to_stack(self.mul_button.text())

    def div_button_fired(self):
        self.test.push_to_stack(self.div_button.text())

    def clr_button_fired(self):
        self.test.clear_stack()

    def equals_button_fired(self):
        self.test.set_result()
        self.textEdit.setText(unicode(self.test.result))
        self.test.clear_stack()
        self.test.push_to_stack(self.test.result)

    def layout(self):

        textlayout = QGridLayout()
	textlayout.addWidget(self.textEdit)
        
        layout = QGridLayout()

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

        mainlayout = QVBoxLayout()
        mainlayout.addLayout(textlayout)
        mainlayout.addLayout(layout)
	
        self.window.setLayout(mainlayout)
        self.window.setWindowTitle("Calculator : Poruri Sai Rahul")

    def main(self):
        
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(unicode(self.test.result))
        
        self._create_buttons()
        self._attach_buttons_to_actions()
        self.layout()
	self.window.show()

	return self.app.exec_()

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo = Application()
    demo.main()
