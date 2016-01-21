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

"""
import os
importList = []
for file in os.listdir('.'):
	if os.path.splitext(file)[1] == '.py':
		importList.append(os.path.splitext(file)[0])

modules = map(__import__, importList)
myattr = getattr(modules[0], importList[0])

http://stackoverflow.com/questions/301134/dynamic-module-import-in-python
http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python
http://www.diveintopython.net/functional_programming/dynamic_import.html
http://stackoverflow.com/questions/11108628/python-dynamic-from-import
http://www.blog.pythonlibrary.org/2012/07/31/advanced-python-how-to-dynamically-load-modules-or-classes/

"""
