# http://doc.qt.io/qt-4.8/gettingstartedqt.html 
# http://zetcode.com/gui/pyqt4/firstprograms/
# https://doc.qt.io/archives/qq/qq19-buttons.html

"""
from pyface.qt.QtGui import QApplication
from pyface.qt.QtGui import QTextEdit

import sys

def main():
	app = QApplication(sys.argv)
	textEdit = QTextEdit()
	textEdit.show()

	app.exec_()
	return
"""

from traits.api import Callable
from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication
import sys

def on_ok():
	print 'yay'

def main():
	app = QApplication(sys.argv)
	textEdit = QTextEdit()
	quitButton = QPushButton("Quit")
	quitButton.clicked.connect(QCoreApplication.instance().quit)

	cancelButton = QPushButton("Cancel")
	okButton = QPushButton("OK")
	okButton.clicked.connect(on_ok)

	box = QDialogButtonBox()
	box.addButton("Apply", QDialogButtonBox().ApplyRole)

	layout = QVBoxLayout()
	layout.addWidget(textEdit)
	layout.addWidget(quitButton)
	layout.addWidget(cancelButton)
	layout.addWidget(okButton)
	layout.addWidget(box)

	window = QWidget()
	window.setLayout(layout)
	window.setWindowTitle("Notepad : Poruri Sai Rahul")

	window.show()

	print on_ok

	return app.exec_()

if __name__ == "__main__":
	main()
