# configure_traits_view.py -- Sample code to demonstrate
#                             configure_traits()

from traits.api import HasTraits, Str, Int, Bool
from traitsui.api import View, Item
import traitsui

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str
    employee_number = Str
    salary = Int
    bool_test = Bool

view1 = View(Item(name = 'first_name', enabled_when = 'bool_test == True'),
             Item(name = 'last_name'),
             Item(name = 'department'),
	     Item(name = 'bool_test'))

sam = SimpleEmployee()
sam.configure_traits(view=view1)
