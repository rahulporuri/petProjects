from model import Application
import unittest

class testModel(unittest.TestCase):
    calculator = Application()

    def test_add(self):
        self.calculator.compute_box = 14
        self.calculator.add_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 34)

        self.calculator.compute_box = 14.0
        self.calculator.add_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 34.0)

        self.calculator.compute_box = 14.65
        self.calculator.add_button_fired()
        self.calculator.compute_box = 20.09
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 34.74)
    
    def test_sub(self):
        self.calculator.compute_box = 14
        self.calculator.subtract_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, -6)

        self.calculator.compute_box = 14.0
        self.calculator.subtract_button_fired()
        self.calculator.compute_box = 10
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 4.0)

        self.calculator.compute_box = 14.65
        self.calculator.subtract_button_fired()
        self.calculator.compute_box = 20.09
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, -5.44)
    
    def test_div(self):
        self.calculator.compute_box = 14
        self.calculator.div_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        # fails because we do floor division for integers!
        self.assertEqual(self.calculator.compute_box, 0.7)

        self.calculator.compute_box = 14.0
        self.calculator.div_button_fired()
        self.calculator.compute_box = 10
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 1.40)

        self.calculator.compute_box = 1
        self.calculator.div_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 0.05)
    
    def test_mul(self):
        self.calculator.compute_box = 14
        self.calculator.mul_button_fired()
        self.calculator.compute_box = 20
        self.calculator.eval_expr()

        # fails because we do floor division for integers!
        self.assertEqual(self.calculator.compute_box, 280)

        self.calculator.compute_box = 14.0
        self.calculator.mul_button_fired()
        self.calculator.compute_box = 10
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 140.0)

        self.calculator.compute_box = 1.1
        self.calculator.mul_button_fired()
        self.calculator.compute_box = 20.4
        self.calculator.eval_expr()

        self.assertEqual(self.calculator.compute_box, 22.44)
