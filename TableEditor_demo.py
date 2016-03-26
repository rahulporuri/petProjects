#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

"""
Implementation of a TableEditor demo plugin for Traits UI demo program

This demo shows the full behavior of a straightforward TableEditor.  Only
one style of TableEditor is implemented, so that is the one shown.
"""

# Import statements:

from numpy \
    import linspace, sin

from traits.api \
    import HasTraits, HasStrictTraits, Instance, Str, Button, Float, List, on_trait_change

from traitsui.api \
    import View, Group, VGroup, HGroup, Item, TableEditor 

from traitsui.table_column \
    import ObjectColumn 

from chaco.api \
    import ArrayPlotData, HPlotContainer, Plot

from enable.component_editor \
    import ComponentEditor

# A helper class for the 'Department' class below:
class row_data( HasTraits ):
    first_name = Str
    last_name  = Str
    age        = Float 

    traits_view = View(
        'first_name', 'last_name', 'age', 'phone',
        title   = 'Create new employee',
        width   = 0.18,
        buttons = [ 'OK', 'Cancel' ]
    )

# The definition of the demo TableEditor:
table_editor = TableEditor(
    columns = [ ObjectColumn( name = 'first_name', width = 0.20 ),
                ObjectColumn( name = 'last_name',  width = 0.20 ),
                ObjectColumn( name = 'age',   width = 0.10,
                              horizontal_alignment = 'center' ),
              ],
    deletable   = True,
    sort_model  = True,
    auto_size   = False,
    orientation = 'vertical',
    show_toolbar = True,
    row_factory = row_data )

# The class to be edited with the TableEditor:
class Department ( HasStrictTraits ):

    aplot = Instance( HPlotContainer )

    rows = List( row_data )
    add_row_button = Button('Add new row')
    print_rows_button = Button('Print row data')

    #@on_trait_change('rows')
    def _make_plot(self):
        #self.rows = rows
        #x = linspace(-14,14,100)
        #y = sin(x)*(x**3)

        x = [row.age for row in self.rows]
        y = [row.age for row in self.rows]

        plotdata = ArrayPlotData(x=x,y=y)

        test_plot = Plot(plotdata)
        test_plot.plot(("x","y"),type="line")

        container = HPlotContainer(test_plot)
        self.aplot = container

    def _rows_changed(self):
        print 1
        self._make_plot()

    def _add_row_button_fired(self):
        self.rows.append(row_data(first_name = '0',
                                 last_name   = '0',
                                 age = 0)
                                )
        self._make_plot()

    def _print_rows_button_fired(self):
        for row in self.rows:
            print row.first_name, row.last_name, row.age
        return

    traits_view = View(
                    HGroup(
                        VGroup(
                            Group(
                                Item('rows',
                                     show_label  = False,
                                     editor = table_editor
                                    ),
                                show_border = True,
                                ),
                            HGroup('add_row_button',
                                   'print_rows_button'
                                  ),
                             ),
                        Group(
                            Item('aplot',
                                editor = ComponentEditor(),
                                width  = 500,
                                height = 500)
                            )
                    ),
                    title     = 'TableEditor',
                    width     = .4,
                    height    = .4,
                    resizable = True,
                    buttons   = [ 'OK' ],
                    kind      = 'live',
                )

# Create some rows
rows = [
    row_data( first_name = 'Jason',
              last_name  = 'Smith',
              age = 32),
    row_data( first_name = 'Mike',
              last_name  = 'Tollan',
              age = 34),
    row_data( first_name = 'Dave',
              last_name  = 'Richards',
              age = 42),
    row_data( first_name = 'Lyn',
              last_name  = 'Spitz',
              age = 40),
    row_data( first_name = 'Greg',
              last_name  = 'Andrews',
              age = 45)
]

# Create the demo:
demo = Department()
demo.rows = rows

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.configure_traits()
