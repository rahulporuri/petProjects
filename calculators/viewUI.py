# Import statements:

from traits.api \
    import HasTraits, HasStrictTraits, Instance, Int, Str, Button, Float, List, on_trait_change, File, Array

from traitsui.api \
    import View, Group, VGroup, HGroup, Item, TableEditor, TextEditor, ArrayEditor

from newModel import Application as calcApp

# The class to be edited with the TableEditor:
class Application ( HasStrictTraits ):

    test = calcApp()
    result = Float

    nine_button = Button('9')
    eight_button = Button('8')
    seven_button = Button('7')
    six_button = Button('6')
    five_button = Button('5')
    four_button = Button('4')
    three_button = Button('3')
    two_button = Button('2')
    one_button = Button('1')
    zero_button = Button('0')

    add_button = Button('+')
    subtract_button = Button('-')
    mul_button = Button('*')
    div_button = Button('/')

    dot_button = Button('.')
    equals_button = Button('=')
    clr_button = Button('clr')

    def _nine_button_fired(self):
        self.test.push_to_stack(int(9))
    
    def _eight_button_fired(self):
        self.test.push_to_stack(int(8))

    def _seven_button_fired(self):
        self.test.push_to_stack(int(7))

    def _six_button_fired(self):
        self.test.push_to_stack(int(6))

    def _five_button_fired(self):
        self.test.push_to_stack(int(5))

    def _four_button_fired(self):
        self.test.push_to_stack(int(4))

    def _three_button_fired(self):
        self.test.push_to_stack(int(3))

    def _two_button_fired(self):
        self.test.push_to_stack(int(2))

    def _one_button_fired(self):
        self.test.push_to_stack(int(1))

    def _zero_button_fired(self):
        self.test.push_to_stack(int(0))

    def _dot_button_fired(self):
        self.test.push_to_stack('.')

    def _add_button_fired(self):
        self.test.push_to_stack('+')

    def _subtract_button_fired(self):
        self.test.push_to_stack('-')

    def _mul_button_fired(self):
        self.test.push_to_stack('*')

    def _div_button_fired(self):
        self.test.push_to_stack('/')

    def _clr_button_fired(self):
        self.test.clear_stack()

    def _equals_button_fired(self):
        self.result = self.test.eval_stack()
    
    traits_view = View(
                    VGroup(
                        HGroup(Item('result', label=" ", 
                               editor=TextEditor()),
                               ),
                        HGroup(Item('nine_button', label=" "), 
                               Item('eight_button', label=" "),
                               Item('seven_button', label=" "),
                        ),
                        HGroup(Item('six_button', label=" "), 
                               Item('five_button', label=" "),
                               Item('four_button', label=" "),
                        ),
                        HGroup(Item('three_button', label=" "), 
                               Item('two_button', label=" "),
                               Item('one_button', label=" "),
                        ),
                        HGroup(Item('mul_button', label=" "), 
                               Item('dot_button', label=" "),
                               Item('div_button', label=" "),
                               ),
                        HGroup(Item('add_button', label=" "), 
                               Item('equals_button', label=" "),
                               Item('subtract_button', label=" "),
                               ),
                        HGroup(Item('zero_button', label=" "),
                               Item('clr_button', label=" "),
                               ),
                    ),
                    resizable = True,
                    buttons   = [ 'OK' ],
                    kind      = 'live',
                )

# Create the demo:
demo = Application()

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.configure_traits()
