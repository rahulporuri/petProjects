from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import ode
import os
import sys
import pdb

'''
Numerical solution of the one-body problem using dopri5
'''
  
 # Compute RHS of ODE, f(t,Y)
def f(t,Y):
	x,y,vx,vy = Y # define individual values
        d3 = (x**2+y**2)**1.5 # ||x||^3
        M = .5
        return array([vx,vy,-M*x/d3,-M*y/d3])
                  
# initial parameters
t0 = 0 # initial start time
tfinal = 5 # final start time
dt = .005 # time step to solution (dopri5 algorithm uses adaptive)
y0 = array([.25,0.0,0.0,.45]) # initial position and velocity
                   
# initiate integrator object
test = ode(f).set_integrator('dopri5',atol=1e-6) # prescribe tolerance for adaptive time step
test.set_initial_value(y0,t0) # set initial time and initial value
         
fig = figure() # initialize figure
ax = fig.add_subplot(111) # name of the plot
while test.successful() and test.t < tfinal:
	# integrate
        test.integrate(test.t+dt)
        # plot position
        ax.plot(test.y[0],test.y[1],'b.',markersize=2)
        ax.plot(0,0,'oy',markersize=12)
        ax.set_xlim([-.15,.35])
        ax.set_ylim([-.12,.15])
        ax.set_title('One-body orbit')
        show() # show plot


# converting png to animated gif
print '\nConverting png files to animated gif (this maye take some time)...\n'
os.system("convert -delay 3 -loop 0 *.png " + "orbit.gif")
os.system("rm *.png *.pyc") # clean up files
os.system("animate orbit.gif") # play animates gif

#pdb.set_trace()
