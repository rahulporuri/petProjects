import matplotlib.pyplot as plt
import numpy

from traits.api import *
import traitsui
from traitsui.api import View, Item
from traitsui.menu import ApplyButton

from ddho_vis import *
from bbrad_vis import *

class visphys(ddho, bbrad, HasTraits):
	"""
	Attributes -
	dis_ddho
	dis_bbrad 

	Methods -
	eval_vis :depending on the values of  
	(dis_ddho and dis_bbrad), this method 
	decides which of the two visualizations, 
	damped-driven harmonic oscillator or 
	blackbody radiation curve, to display.
	_dis_ddho_changed : checks for changes 
	in dis_ddho and updates the plot corrspondingly
	_dis_bbrad_changed : checks for changes 
	in dis_bbrad and updates the plot corrspondingly
	"""

	dis_ddho = Bool
	dis_bbrad = Bool

#	def __init__(self):
#		ddho.__init__(self)
#		bbrad.__init__(self)

#	def eval_vis(self):
#		""" for a specific set of (dis_ddro, dis_bbrad) 
#		values, this method decides which of the two
#		visualizations to display."""
#	"""		
#		if self.dis_ddho == True:
#			ddho_inst = ddho()
#			ddho_inst.configure_traits()
#		elif self.dis_bbrad == True:
#			bbrad_inst = bbrad()
#			bbrad_inst.configure_traits()
#
#	def _changed(self):
#		"""checks for changes in dis_ddho
#		and updates the plot corrspondingly
#		if self.dis_ddho == True:
#			print 'displaying the damped-driven oscillator visualization'"""
#		self.eval_vis()
#
#	def _dis_bbrad_changed(self):"""
#		""" checks for changes in dis_bbrad 
#		and updates the plot corrspondingly"""
#	"""		if self.dis_bbrad == True:
#			print 'displaying the blackbody raditaion curve visualization'
#		self.eval_vis()                               """

ddho_inst = ddho()
bbrad_inst = bbrad()

view1 = View(Item(name = 'dis_ddho'),
		Item(name = 'dis_bbrad'),
		Item(name = 'k', enabled_when = 'dis_ddho == True'),
		Item(name = 'a', enabled_when = 'dis_ddho == True'),
		Item(name = 'T', enabled_when = 'dis_bbrad == True'),
		buttons = [ApplyButton])

visphys_inst = visphys()
visphys_inst.configure_traits(view = view1)
