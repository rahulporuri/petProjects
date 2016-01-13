# all_traits_features.py 

from traits.api import Delegate, HasTraits, Instance, Int, Str
import traitsui

import matplotlib.pyplot as plt
import numpy

h = 0.01
m = 1.
a = 1.


def fn(k,m,a,x,dx):
    return -k*x/m -a*dx/m

def rk2_step(k, m, a, x, dx):
        F1 = dx
        f1 = fn(k, m, a, x, dx)
        F2 = dx +f1*h
        f2 = fn(k, m, a, x +F1*h, dx +f1*h)
        return (f1 +f2)*h/2., (F1 +F2)*h/2.
        # (dy, y) update

class Child(HasTraits):
    age = Int

    def eval_plot(self):
	x = []
	t = numpy.linspace(0,1,101)
	xi = 0.
	dxi = 1.
	k = self.age
	i = 0
	while i < len(x):
		y.append(yi)
		dyi_inc, yi_inc = rk2_step(k,m,a,yi,dyi)
		dyi += dyi_inc
		yi += yi_inc
		i += 1
	plt.plot(x,numpy.asarray(y))
	plt.show()

    def _age_changed(self, old, new): 
        print 'Age changed from %s to %s ' % (old, new)
	self.eval_plot()

moe = Child()
moe.age = 10

moe.configure_traits()
