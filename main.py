import matplotlib.pyplot as plt
import numpy

from traits.api import *
import traitsui
from traitsui.api import View, Item, Group

from ddho_vis import *
from bbrad_vis import *

class visphys(ddho, bbrad, HasTraits):
	"""
	Attributes -
	dis_ddho
	dis_bbrad 
	"""

	dis_ddho = Bool
	dis_bbrad = Bool

view1 = View(Item(name = 'dis_ddho'),
		Item(name = 'dis_bbrad'),
		Item(name = 'k', enabled_when = 'dis_ddho == True'),
		Item(name = 'a', enabled_when = 'dis_ddho == True'),
		Item(name = 'T', enabled_when = 'dis_bbrad == True'),
	)

view2 = View(Group(Item(name = 'T')),
                Group(Item(name = 'k'),
                     Item(name = 'a')),
        )

visphys_inst = visphys()
visphys_inst.configure_traits(view = view2)
