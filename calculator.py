# Import statements:

from traits.api \
    import HasTraits, HasStrictTraits, Instance, Int, Str, Button, Float, List, on_trait_change, File, Array

from traitsui.api \
    import View, Group, VGroup, HGroup, Item, TableEditor, TextEditor, ArrayEditor

# The class to be edited with the TableEditor:
class Application ( HasStrictTraits ):
    compute_box = Float(0.0) 
    temp = Float(0.0)
    count = Int(0)
    dot = Int(-1)

    nine_button = Button('9')
    eight_button = Button('8')
    seven_button = Button('7')
    six_button = Button('6')
    five_button = Button('5')
    four_button = Button('4')
    three_button = Button('3')
    two_button = Button('2')
    one_button = Button('1')

    equals_button = Button('=')
    add_button = Button('+')
    subtract_button = Button('-')
    mul_button = Button('*')
    div_button = Button('/')
    zero_button = Button('0')
    dot_button = Button('.')

    clr_button = Button('clr')

    def _nine_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +9.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +9.0)/10**(self.dot)
            self.dot +=1

    def _eight_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +8.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +8.0)/10**(self.dot)
            self.dot +=1

    def _seven_button_fired(self):
        if self.dot == -1:
            self.compute_box = self.compute_box*10 +7.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +7.0)/10**(self.dot)
            self.dot +=1

    def _six_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +6.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +6.0)/10**(self.dot)
            self.dot +=1

    def _five_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +5.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +5.0)/10**(self.dot)
            self.dot +=1

    def _four_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +4.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +4.0)/10**(self.dot)
            self.dot +=1

    def _three_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +3.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +3.0)/10**(self.dot)
            self.dot +=1

    def _two_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +2.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +2.0)/10**(self.dot)
            self.dot +=1

    def _one_button_fired(self):
        if self.dot == -1: 
            self.compute_box = self.compute_box*10 +1.0
        else:
            self.compute_box = (self.compute_box*10**(self.dot) +1.0)/10**(self.dot)
            self.dot +=1

    def _zero_button_fired(self):
        # does some weird shit!
        if self.dot == -1: 
            self.compute_box = self.compute_box*10
#        else:
            # dunno what to do when we want to add 
            # after zero!

    def _dot_button_fired(self):
            self.dot = 1

    @on_trait_change('equals_button')
    def eval_expr(self):
        if self.count == 1:
            self.compute_box += self.temp
        elif self.count == -1:
            self.compute_box -= self.temp
        elif self.count == 2:
            self.compute_box = self.compute_box*self.temp
        elif self.count == -2:
            self.compute_box = self.temp/self.compute_box

    def _add_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 1
        self.dot = -1

    def _subtract_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -1
        self.dot = -1

    def _mul_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = 2
        self.dot = -1

    def _div_button_fired(self):
        self.temp = self.compute_box
        self.compute_box = 0.0
        self.count = -2
        self.dot = -1

    def _clr_button_fired(self):
        self.temp = 0.0
        self.compute_box = 0.0
        self.count = 0
        self.dot =-1 

    traits_view = View(
                    VGroup(
                        HGroup(Item('compute_box', label=" ", 
                               editor=TextEditor()),
                               Item('temp', label=" ",
                               editor=TextEditor(),
                               style="readonly")
                               ),
                        HGroup(
                            Group(
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
                                )
                            ),
                            VGroup(Item('zero_button', label=" "),
                                   Item('clr_button', label=" "),
                            ),
                            ),
                        HGroup(Item('mul_button', label=" "), 
                               Item('dot_button', label=" "),
                               Item('div_button', label=" "),
                               ),
                        HGroup(Item('add_button', label=" "), 
                               Item('equals_button', label=" "),
                               Item('subtract_button', label=" "),
                               )
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
