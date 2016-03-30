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

import time 
import sys

from traits.api import Callable
from pyface.qt.QtGui import *
from pyface.qt.QtCore import QCoreApplication

class mainclass():

    app = QApplication(sys.argv)
    textEdit = QTextEdit()


    progressBar = QProgressBar()

    def on_ok(self):
    	print 'yay'

    def on_quit(self):
	messageBox = QMessageBox()
        messageBox.setWindowTitle("Quit Notepad")
	messageBox.setText("Do you really want to quit?")
	messageBox.setStandardButtons(QMessageBox().Yes | QMessageBox().No)
	messageBox.setDefaultButton(QMessageBox().No)
	if messageBox.exec_() == QMessageBox().Yes:
		qApp.quit()

    def on_cancel(self):
        print 'do you want to cancel?'

    def on_print(self):
        print self.textEdit.toPlainText()

    def updateProgressBar(self):
        for i in range(100):
            self.progressBar.setValue(i)
            time.sleep(1)

# doesnt work
    def on_openfile(self):
        filedialog = QFileDialog()
        layout = QVBoxLayout()
        layout.addWidget(filedialog)
        widget = QWidget()
        widget.setLayout(layout)
        widget.show


    def main(self):
	quitButton = QPushButton("Quit")
#	quitButton.clicked.connect(QCoreApplication.instance().quit)
	quitButton.clicked.connect(self.on_quit)

	cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.on_cancel)
        okButton = QPushButton("OK")
	okButton.clicked.connect(self.on_ok)
        printButton = QPushButton("Print")
        printButton.clicked.connect(self.on_print)

        updateProgressBarButton = QPushButton("Update Progress Bar")
        updateProgressBarButton.clicked.connect(self.updateProgressBar)

        box = QDialogButtonBox()
	box.addButton("Apply", QDialogButtonBox().ApplyRole)

        filedialog = QFileDialog()
        openfile = QPushButton("Open file")
        openfile.clicked.connect(self.on_openfile)

	layout = QVBoxLayout()
        layout.addWidget(filedialog)
        layout.addWidget(openfile)
	layout.addWidget(self.textEdit)
	layout.addWidget(quitButton)
	layout.addWidget(cancelButton)
	layout.addWidget(okButton)
        layout.addWidget(printButton)
        layout.addWidget(self.progressBar)
        layout.addWidget(updateProgressBarButton)
        layout.addWidget(box)

	window = QWidget()
	window.setLayout(layout)
	window.setWindowTitle("Notepad : Poruri Sai Rahul")

	window.show()

	return self.app.exec_()

if __name__ == "__main__":
	test = mainclass()
        test.main()

