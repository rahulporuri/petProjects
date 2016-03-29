# http://matplotlib.org/examples/pylab_examples/fill_between_demo.html

import matplotlib.pyplot as plt
import numpy

fig,ax = plt.subplots(1,1,sharex=True)
ax.set_xlim([-10,10])
ax.set_ylim([-2,2])

x = numpy.arange(-5,5)
y1 = -1
y2 = 1

ax.fill_between(x,y1,y2)
plt.show()
