# all_traits_features.py 

from traits.api import Delegate, HasTraits, Instance, Int, Str
import traitsui

from traitsui.api import View, Item, ButtonEditor

import matplotlib.pyplot as plt
import numpy

class Parent(HasTraits):

    # INITIALIZATION: last_name' is initialized to '':
    last_name = Str('')

h = 0.01
m = 1.
a = 1.

#assume alpha = 1
def fn(k,m,a,y,dy):
    return -k*y/m -a*dy/m

def euler_step(k,m,a,y,dy):
    F1 = dy
    f1 = fn(k,m,a,y,dy)
    return [f1*h, F1*h] # [dy, y] update

class Child(HasTraits):
    age = Int

    start_stop_capture = Button()
    view = View(Item('start_stop_capture', show_label = False))

    def _start_stop_capture_fired(self):
        if self.capture_thread and self.capture_thread.isAlive():
            self.capture_thread.wants_abort = True
        else:
            self.capture_thread = CaptureThread()
            self.capture_thread.wants_abort = False
            self.capture_thread.display = self.display
            self.capture_thread.start()

    # VALIDATION: 'father' must be a Parent instance:
    father = Instance(Parent)

    # DELEGATION: 'last_name' is delegated to father's 'last_name':
    last_name = Delegate('father')

    def eval_plot(self):
	y = []
	x = numpy.linspace(0,1,101)
	yi = 0.
	dyi = 1.
	k = self.age
	i = 0
	while i < len(x):
		y.append(yi)
		dyi_inc, yi_inc = euler_step(k,m,a,yi,dyi)
		dyi += dyi_inc
		yi += yi_inc
		i += 1
	plt.plot(x,numpy.asarray(y))
	plt.show()

    # NOTIFICATION: This method is called when 'age' changes:
    def _age_changed(self, old, new): 
        print 'Age changed from %s to %s ' % (old, new)
	self.eval_plot()
#	plt.plot(numpy.linspace(0,1,11), self.age*numpy.linspace(0,1,11))
#	plt.show()

# Set up the example:
joe = Parent()
joe.last_name = 'Johnson'
moe = Child()
moe.father = joe
	
# DELEGATION in action:
print "Moe's last name is %s" % moe.last_name

# NOTIFICATION in action:
moe.age = 10

# VISUALIZATION: Displays a UI for editing moe's 
# attributes (if a supported GUI toolkit is installed)
moe.configure_traits()
