import unittest

from traits.api import HasTraits, Int, Float


class mathOps(HasTraits):
    #a = Int
    a = Float
    #b = Int
    b = Float

    def add(self, a, b):
        self.a = a
        self.b = b

        return self.a +self.b

    def sub(self, a, b):
        self.a = a
        self.b = b

        return self.a -self.b

    def mul(self, a, b):
        self.a = a
        self.b = b

        return self.a*self.b

    def div(self, a, b):
        self.a = a
        self.b = b

        return self.a/self.b

class mathOpsTest(unittest.TestCase):
    obj = mathOps()

    def test_add(self):
        self.assertEqual(self.obj.add(1,1), 2)
        self.assertEqual(self.obj.add(1,2.0), 3.0)
        self.assertEqual(self.obj.add(3.0,1), 4.0)
        self.assertEqual(self.obj.add(5.0,6.0), 11.0)

    def test_sub(self):
        self.assertEqual(self.obj.sub(1,1), 0)
        self.assertEqual(self.obj.sub(1,2.0), -1.0)
        self.assertEqual(self.obj.sub(3.0,1), 2.0)
        self.assertEqual(self.obj.sub(4.0,8.0), -4.0)

    def test_mul(self):
        self.assertEqual(self.obj.mul(1,1), 1)
        self.assertEqual(self.obj.mul(1,2.0), 2.0)
        self.assertEqual(self.obj.mul(4.0,2), 8.0)
        self.assertEqual(self.obj.mul(3.0,7.0), 21.0)

    def test_div(self):
        self.assertEqual(self.obj.div(1,1), 1)
        self.assertEqual(self.obj.div(1.0,2), 0.5)
        self.assertEqual(self.obj.div(1,10.0), 0.1)
        self.assertEqual(self.obj.div(1.0,5.0), 0.2)

    @unittest.expectedFailure
    def test_vector_add(self):
        self.assertIsInstance(self.a, )
        self.assertEqual(self.obj.add([1,1],[1,1]),[2,2])
