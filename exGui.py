# http://doc.qt.io/qt-4.8/gettingstartedqt.html 
# http://zetcode.com/gui/pyqt4/firstprograms/

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

from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication
import sys

def main():
	app = QApplication(sys.argv)
	textEdit = QTextEdit()
	quitButton = QPushButton("Quit")
	quitButton.clicked.connect(QCoreApplication.instance().quit)

	cancelButton = QPushButton("Cancel")
	okButton = QPushButton("OK")

	layout = QVBoxLayout()
	layout.addWidget(textEdit)
	layout.addWidget(quitButton)
	layout.addWidget(cancelButton)
	layout.addWidget(okButton)

	window = QWidget()
	window.setLayout(layout)
	window.setWindowTitle("Notepad : Poruri Sai Rahul")

	window.show()

	return app.exec_()

if __name__ == "__main__":
	main()
