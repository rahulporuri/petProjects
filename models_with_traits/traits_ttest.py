from traits.api import *
from traitsui.api import *

class Camera(HasTraits):
    """ Camera object """

    gain = Enum('one', 'two', 'three',
        desc="the gain index of the camera",
        label="gain",
	style = 'custom',
	cols = 3,)

    rangetest = Range(1,10)

    booltest = Bool

    exposure = CInt(10,
        desc="the exposure time, in ms",
        label="Exposure", )

    def capture(self):
        """ Captures an image on the camera and returns it """
        print "capturing an image at %i ms exposure, gain: %s" % (
                self.exposure, self.gain )

    def _gain_changed(self, old, new):
	if self.gain == 'one':
		print '1'
	elif self.gain == 'two':
		print '2'
	elif self.gain == 'three':
		print '3'

    def _booltest_changed(self, old, new):
	if self.booltest == True:
		print 'True'
	else:
		print 'False'

    def _rangetest_changed(self, old, new):
	print "%s to %s"%(old, new)

if __name__ == "__main__":
    camera = Camera()
    camera.configure_traits()
    camera.capture()
