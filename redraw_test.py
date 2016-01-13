from matplotlib import pyplot as plt
import numpy

f = plt.figure()
ax = f.gca()
f.show()

x = numpy.linspace(0,1,101)
y = numpy.linspace(0,1,101)

for i in range(10):
    ax.plot(x, y*i/5, 'ko')
    f.canvas.draw()
    raw_input('pause : press any key ...')
f.close()

