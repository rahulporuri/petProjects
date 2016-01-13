from traits.api import HasTraits, Bool, Float, Range
from traitsui.api import View, Item, Group

import matplotlib.pyplot as plt
import numpy

step = 0.01			# step size for the rk4 stepper
m = 1.				# mass of the object undergoing 
				# damped driven harmonic oscillations

h = 6.6244e-34 # Planck constant in Js
c = 2.998e+08     # speed of light in m/s
kb = 1.38e-23    #Boltzmann constant in J/K%

def ddx(k, m, a, x, dx):
	"""function that estimates the 
	second derivative of the position x"""
	return -k*x/m -a*dx/m

def rk4_step(k, m, a, x, dx):
	"""function that updates the position x
	using a runge-kutta 2 method"""
	F1 = dx
	f1 = ddx(k, m, a, x, dx)
	F2 = dx +f1*step/2.
	f2 = ddx(k, m, a, x +F1*step/2., dx +f1*step/2.)
	F3 = dx +f2*step/2.
	f3 = ddx(k, m, a, x +F2*step/2., dx +f2*step/2.)
	F4 = dx +f3*step
	f4 = ddx(k, m, a, x +F3*step, dx +f3*step)

	return (f1 +2*f2 +2*f3 +f4)*step/6., (F1 +2*F2 +2*F3 +F4)*step/6. 
	# (dy, y) update

class Models(HasTraits):
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
	disp_bbrad = Bool
	disp_ddho = Bool

	k = Float
	a = Float
	T = Range(1,9)

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
			dxi_inc, xi_inc = rk4_step(k,m,a,xi,dxi)
			dxi += dxi_inc
			xi += xi_inc
			i += 1
		plt.plot(t, numpy.asarray(x),label=('k=',self.k,'a=',self.a))
		plt.legend(loc = 'upper right')
		plt.xlabel('time t')
		plt.ylabel('position x')
		plt.show()

        def bbradfn(self, lamda, T):
                """bbradfn : a function that defines the 
                amount of radiation emitted by a blackbody 
                as a function of temperature and wavelength."""
                return (2*h*c*c)/(((lamda*1e-10)**5)*(numpy.exp(h*c/(lamda*1e-10*kb*T))-1))

        def eval_bbrad_plot(self):
                """ for a specific set of 
                T value, this method evaluates the amount 
                of radiation emitted by a blackbody."""

                lamda = numpy.linspace(1000,10000,100)
                plt.plot(lamda, self.bbradfn(lamda, self.T*10**3), label=('T=',self.T*10**3))
                plt.legend(loc = 'upper right')
                plt.xlabel('wavelength')
                plt.ylabel('intensity I')
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

        def _T_changed(self, old, new):
                """checks for changes in k 
                and updates the plot corrspondingly"""
                print 'the temperature of the blackbody emitter : T has been changed from %s to %s ' % (old, new)
                self.eval_bbrad_plot()

view1 = View(Item(name = 'disp_bbrad'),
	     Item(name = 'T', enabled_when = 'disp_bbrad == True'),
	     Item(name = 'disp_ddho'),
	     Item(name = 'k', enabled_when = 'disp_ddho == True'),
	     Item(name = 'a', enabled_when = 'disp_ddho == True'),
	)

view2 = View(Group(Item(name = 'T')),
		Group(Item(name = 'k'),
	             Item(name = 'a')),
	)

model_inst = Models()
model_inst.configure_traits(view = view2)
