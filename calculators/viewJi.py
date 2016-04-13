"""
This example shows how to use Jigna alongwith a custom angularjs application. We
would need a custom angularjs application to add some view related logic.
"""

#### Imports ####

import sys
from jigna.api import HTMLWidget, Template
from jigna.qt import QtGui
import time
from traits.api import HasTraits, Float, List

from newModel import Application as calcApp

#### Domain model ####

class StopWatch(HasTraits):

    result = Float
    stack = List 

    def push_to_stack(self, item):
        self.stack.append(item)

    def eval_stack(self):
        i = 0           # counter to keep track of decimal point
        temp = 0        # counter to keep track of current input
        temp2 = 0       # counter to store previous input
        op = ''         # used to store the math operator
        while self.stack != []:
           if not isinstance(self.stack[-1], unicode) :
               temp += self.stack.pop()*10**i
               i += 1
           else :
               if self.stack[-1] == '.':
                   self.stack.pop()
                   temp = temp/(10.**(i))
                   i = 0
               else :
                   op = self.stack.pop()
                   temp2 = temp
                   temp = 0
                   i = 0

        if op == '+':
            return temp2 + temp
        elif op == '-':
            return temp - temp2
        elif op == '*':
            return temp*temp2
        elif op == '/':
            return float(temp)/temp2

    def set_result(self):
        self.result = self.eval_stack()

    def clear_stack(self):
        self.stack = []

#### UI layer ####

template = Template(html_file='custom_angular_application.html')

#### Entry point ####

def main():
    # Start the Qt application
    app = QtGui.QApplication(sys.argv)

    # Instantiate the domain model
    stop_watch = StopWatch()
    #stop_watch = calcApp()

    # Create the jigna based HTML widget which renders the given HTML template
    # with the given context.
    #
    # The operations on the stop watch can be controlled from the UI. The view
    # related logic is such that it always displays the integer time of the
    # domain model in a proper hh:mm:ss format.
    widget = HTMLWidget(template=template, context={'stop_watch': stop_watch})
    widget.show()

    # Start the event loop
    app.exec_()

    # Check the values after the UI is closed
    print stop_watch.stack, "are the contents of the stack"
    print stop_watch.result

if __name__ == "__main__":
    main()

#### EOF ######################################################################
