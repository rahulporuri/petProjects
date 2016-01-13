from traits.api import *
import traitsui

import matplotlib.pyplot as plt
import numpy

h = 0.01			# step size for the rk4 stepper
m = 1.				# mass of the object undergoing 
				# damped driven harmonic oscillations

def ddx(k, m, a, x, dx):
	"""function that estimates the 
	second derivative of the position x"""
	return -k*x/m -a*dx/m

def rk2_step(k, m, a, x, dx):
	"""function that updates the position x
	using a runge-kutta 2 method"""
	F1 = dx
	f1 = ddx(k, m, a, x, dx)
	F2 = dx +f1*h
	f2 = ddx(k, m, a, x +F1*h, dx +f1*h)
	
	return (f1 +f2)*h/2., (F1 +F2)*h/2. 
	# (dy, y) update

class ddho(HasTraits):
	"""
	Attributes -
	k : strength of force constant
	a : strength of damping term

	Methods -
	eval_plot : for a specific set of 
	(k,a), values, this method evaluates 
	the position x of the ddho with time t
	_k_changed : checks for changes in k 
	and updates the plot corrspondingly
	_a_changed : checks for changes in a 
	and updates the plot corrspondingly
	"""
	k = Float
	a = Float

	def eval_ddho_plot(self):
		""" for a specific set of 
		(k,a), values, this method evaluates 
		the position x of the ddho with time t"""
		
		x = []
		t = numpy.linspace(0,1,101)
		xi = 0.
		dxi = 1.
		k = self.k
		a = self.a
		i = 0
		while i < len(t):
			x.append(xi)
			dxi_inc, xi_inc = rk2_step(k,m,a,xi,dxi)
			dxi += dxi_inc
			xi += xi_inc
			i += 1
		plt.plot(t, numpy.asarray(x),label=('k=',self.k,'a=',self.a))
		plt.legend(loc = 'upper right')
		plt.xlabel('time t')
		plt.ylabel('position x')
		plt.show()

	def _k_changed(self, old, new):
		"""checks for changes in k 
		and updates the plot corrspondingly"""
		print 'the force constant : k has been changed from %s to %s ' % (old, new)
		self.eval_ddho_plot()

	def _a_changed(self, old, new):
		"""checks for changes in a 
		and updates the plot corrspondingly"""
		print 'the damping parameter : a has been changed from %s to %s ' % (old, new)
		self.eval_ddho_plot()                               

# uncomment the following lines
# if you are interested in running 
# this file individually
#
# ddho_inst = ddho()
# ddho_inst.configure_traits()
