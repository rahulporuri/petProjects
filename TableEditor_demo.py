#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

"""
Implementation of a TableEditor demo plugin for Traits UI demo program

This demo shows the full behavior of a straightforward TableEditor.  Only
one style of TableEditor is implemented, so that is the one shown.
"""

# Import statements:

from numpy \
    import linspace, sin, asarray

from scipy.interpolate \
    import interp1d

from traits.api \
    import HasTraits, HasStrictTraits, Instance, Int, Str, Button, Float, List, on_trait_change, File, Array

from traitsui.api \
    import View, Group, VGroup, HGroup, Item, TableEditor, TextEditor 

from traitsui.table_column \
    import ObjectColumn 

from chaco.api \
    import ArrayPlotData, HPlotContainer, ToolbarPlot, ArrayDataSource, DataRange1D, LinearMapper, BarPlot, Plot, PlotGraphicsContext

from chaco.tools.api \
    import SaveTool

from chaco.shell import plot, hold

from enable.component_editor \
    import ComponentEditor

# A helper class for the 'Application' class below:
class row_data( HasTraits ):
    x = Int
    y = Float
    z = Float 

# The definition of the demo TableEditor:
table_editor = TableEditor(
    columns = [ ObjectColumn( name = 'x', width = 0.20 ),
                ObjectColumn( name = 'y',  width = 0.20 ),
                ObjectColumn( name = 'z',   width = 0.10,
                              horizontal_alignment = 'center' ),
              ],
    deletable   = True,
    sort_model  = True,
    auto_size   = False,
    orientation = 'vertical',
    show_toolbar = True,
    row_factory = row_data )

# The class to be edited with the TableEditor:
class Application ( HasStrictTraits ):
    rows = List( row_data )
    aplot = Instance( HPlotContainer )

    #filename = Str
    filename = File

    add_row_button = Button('Add new row')
    print_rows_button = Button('Print row data')
    save_data_button = Button('Save data set')
    load_data_button = Button('Load data set')
    
    save_image_button = Button('Save Plot')
    interp_data_button = Button('Interpolate data')

    @on_trait_change('rows.*')
    def _make_plot(self):
        x = [row.x for row in self.rows]
        y = [row.y for row in self.rows]
        z = [row.z for row in self.rows]

        plotdata = ArrayPlotData(x=x,y=y)
        """
        idx = linspace(1,len(x),len(x))
        vals = z

        bar_width = 1.0
        line_width = 5.0

        index = ArrayDataSource(idx)
        index_range = DataRange1D(index)
        index_mapper = LinearMapper(range=index_range)
        
        value = ArrayDataSource(vals)
        value_range = DataRange1D(value)
        value_mapper = LinearMapper(range=value_range)

        test_plot = BarPlot(index=index, value=value,
                        value_mapper = value_mapper,
                        index_mapper=index_mapper,
                        bgcolor="white",
                        line_color="black",
                        fill_color="cornflowerblue",
                        bar_width=bar_width,
                        line_width=line_width)
        """
        test_plot = ToolbarPlot(plotdata)
        test_plot.plot(("x","y"),type="scatter")
        # changing type to line will make the 
        # plot a line plot! not recommended!

        container = HPlotContainer(test_plot)
        self.aplot = container

    def _save_data_button_fired(self, filename='test.dat'):
        f = open('test.dat', 'w')
        for row in self.rows:
            f.write(str(row.x)+','+str(row.y)+','+str(row.z)+'\n')
        f.close()

    def _load_data_button_fired(self):
        filedialog = FileEditorDemo()
        filedialog.configure_traits

        for line in open(self.filename, 'r'):
            x,y,z = line.split(',')
            self.rows.append(row_data(x=int(x),
                                      y=float(y),
                                      z=float(z)
                                     )
            )

    def _interp_data_button_fired(self):
        x = [row.x for row in self.rows]
        y = [row.y for row in self.rows]

        f = interp1d(asarray(x),asarray(y))
        y2 = Array
        print x, sorted(x)
        y2 = [f(i) for i in sorted(x)]

        print y2
        
        plotdata = ArrayPlotData(x=x,y=y)
        plotdata2 = ArrayPlotData(y=y2)

        test_plot = Plot(plotdata)
        test_plot.plot(("x","y"),type="scatter")
        test_plot.plot(("x","y"),type="line")
        test_plot_2 = Plot(plotdata2)
        #test_plot_2.plot("y2", type="line")
        # changing type to line w)ill make the 
        # plot a line plot! not recommended!
        """
        test_plot = plot(x,y,"b-", bgcolor="white")
        test_plot.hold()
        test_plot = plot(x,y2,"g-")
        """
        container = HPlotContainer(test_plot)#,test_plot_2)
        self.aplot = container

    def _save_image_button_fired(self, filename='test.png'):
        """
        plot = self.aplot
        plot.outer_bounds = [100,100]
        plot.do_layout(force=True)
        gc = PlotGraphicsContext((100,100),dpi=72)
        gc.render_component(plot)
        gc.save(filename)
        """
        plot = self.aplot
        save(filename)

    def _rows_changed(self):
        print 1
        self._make_plot()

    def _add_row_button_fired(self):
        self.rows.append(row_data(x = 0,
                                  y = 0,
                                  z = 0)
                        )
#        self._make_plot()

    def _print_rows_button_fired(self):
        for row in self.rows:
            print row.x, row.y, row.z

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
                                   'print_rows_button',
                                   'save_data_button'
                                  ),
                            HGroup('load_data_button',
                                Item('filename'),
                                #Item('filename',style='custom')
                                )
                             ),
                        VGroup(
                            Item('aplot',
                                editor = ComponentEditor(),
                                width  = 600,
                                height = 600),
                            HGroup('save_image_button',
                                   'interp_data_button')
                            )
                    ),
                    title     = 'TableEditor',
                    width     = .4,
                    height    = .4,
                    resizable = True,
                    buttons   = [ 'OK' ],
                    kind      = 'live',
                )


# Define the demo class:
class FileEditorDemo ( HasTraits ):
    """ Defines the main FileEditor demo class. """

    # Define a File trait to view:
    file_name = File

    # Demo view:
    view = View(
        Item( 'file_name', style = 'custom',   label = 'Custom' ),
        title     = 'FileEditor',
        buttons   = ['OK'],
        resizable = True
    )

# Create some rows
rows = [
    row_data( x = 10,
              y = 11,
              z = 32),
    row_data( x = 14,
              y = 67,
              z = 34),
    row_data( x = 44,
              y = 21,
              z = 42),
    row_data( x = 77,
              y = 54,
              z = 40),
    row_data( x = 22,
              y = 33,
              z = 45)
]

# Create the demo:
demo = Application()
demo.rows = rows

# Run the demo (if invoked from the command line):
if __name__ == '__main__':
    demo.configure_traits()
