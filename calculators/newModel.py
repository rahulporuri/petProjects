"""
Improvements :
    1. Ability to chain/evaluate multiple ops in the same stack! 
"""
import unittest

class Application():

    stack = []
    result = 0

    def push_to_stack(self, to_be_added):
        self.stack.append(to_be_added)

    def eval_stack(self):
        i = 0           # counter to keep track of decimal point
        temp = 0        # counter to keep track of current input
        temp2 = 0       # counter to store previous input
        op = ''         # used to store the math operator
        while self.stack != []:
           if not isinstance(self.stack[-1], basestring):
               temp += self.stack.pop()*10**i
               i += 1
           else :
               if self.stack[-1] == '.':
                   self.stack.pop()
                   temp = temp/(10.**(i))
                   i = 0
               else :
                   op = self.stack.pop()
                   temp2 = temp
                   temp = 0
                   i = 0

        if op == '+':
            return temp2 + temp
        elif op == '-':
            return temp - temp2
        elif op == '*':
            return temp*temp2
        elif op == '/':
            return float(temp)/temp2

    def set_result(self):
        self.result = self.eval_stack()

    def clear_stack(self):
        self.stack = []

class testApplication(unittest.TestCase):

    def test_add(self):
        test = Application()
        test.stack = [1,2,'+',3,4]
        self.assertEqual(test.eval_stack(), 46)

    def test_add_float(self):
        test = Application()
        test.stack = [1,2,'.',4,'+',3,4,'.',5]
        self.assertEqual(test.eval_stack(), 46.9) 
    
    def test_sub(self):
        test = Application()
        test.stack = [1,2,'-',3,4]
        self.assertEqual(test.eval_stack(), -22)

    def test_sub_float(self):
        test = Application()
        test.stack = [1,2,'.',4,'-',3,4,'.',5]
        self.assertEqual(test.eval_stack(), -22.1)
    
    def test_mul(self):
        test = Application()
        test.stack = [1,2,'*',4]
        self.assertEqual(test.eval_stack(), 48)

    def test_mul_float(self):
        test = Application()
        test.stack = [1,'.',4,'*',3,'.',5]
        self.assertEqual(test.eval_stack(), 4.9)
    
    def test_div(self):
        test = Application()
        test.stack = [1,2,'/',4]
        self.assertEqual(test.eval_stack(), 3.0)

    def test_div_float(self):
        test = Application()
        test.stack = [1,'/',5]
        self.assertEqual(test.eval_stack(), 0.2)
