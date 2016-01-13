from traits.api import *
import traitsui

import matplotlib.pyplot as plt
import numpy

h=6.6244e-34 # Planck constant in Js
c=2.998e+08     # speed of light in m/s
k=1.38e-23    #Boltzmann constant in J/K%

class bbrad(HasTraits):
	"""
	Attributes -
	T : temperature of the emitter

	Methods -
	bbradfn : a function that defines the 
	amount of radiation emitted by a blackbody 
	as a function of temperature and wavelength.
	eval_plot : for a specific set of 
	T value, this method evaluates 
	the blackbody radiation emitted by the
	body as a function of wavelength.
	_T_changed : checks for changes in T 
	and updates the plot corrspondingly
	"""
	T = Float
#	T = Range(3000,10000)

	def bbradfn(self, lamda, T):
		"""bbradfn : a function that defines the 
		amount of radiation emitted by a blackbody 
		as a function of temperature and wavelength."""
		return (2*h*c*c)/(((lamda*1e-10)**5)*(numpy.exp(h*c/(lamda*1e-10*k*T))-1))

	def eval_plot(self):
		""" for a specific set of 
		T value, this method evaluates the amount 
		of radiation emitted by a blackbody."""
		
		lamda = numpy.linspace(1000,10000,100)
		plt.plot(lamda, self.bbradfn(lamda, self.T), label=('T=',self.T))
		plt.legend(loc = 'upper right')
		plt.xlabel('wavelength')
		plt.ylabel('intensity I')
		plt.show()

	def _T_changed(self, old, new):
		"""checks for changes in k 
		and updates the plot corrspondingly"""
		print 'the temperature of the blackbody emitter : T has been changed from %s to %s ' % (old, new)
		self.eval_plot()

# uncomment the following lines 
# if you are interested in running 
# this files individually
#
# bbrad_inst = bbrad()
# bbrad_inst.configure_traits()
