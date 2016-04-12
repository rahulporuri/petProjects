import unittest

class Application():

    inputstack = []

    def eval_stack(self):
        i = 0           # counter to keep track of decimal point
        temp = 0        # counter to keep track of current input
        temp2 = 0       # counter to store previous input
        op = ''         # used to store the math operator
        while self.inputstack != []:
           if not isinstance(self.inputstack[-1], basestring):
               temp += int(self.inputstack.pop())*10**i
               i += 1
               print temp
           else :
               if self.inputstack[-1] == '.':
                   self.inputstack.pop()
                   temp = temp/(10.**(i))
                   i = 0
                   print temp
               else :
                   op = self.inputstack.pop()
                   temp2 = temp
                   temp = 0
                   i = 0
                   print op, temp, temp2

        if op == '+':
            return temp2 + temp
        elif op == '-':
            return temp - temp2
        elif op == '*':
            return temp*temp2
        elif op == '/':
            return float(temp)/temp2

class testApplication(unittest.TestCase):

    def test_add(self):
        test = Application()
        test.inputstack = [1,2,'+',3,4]
        self.assertEqual(test.eval_stack(), 46)

    def test_add_float(self):
        test = Application()
        test.inputstack = [1,2,'.',4,'+',3,4,'.',5]
        self.assertEqual(test.eval_stack(), 46.9) 
    
    def test_sub(self):
        test = Application()
        test.inputstack = [1,2,'-',3,4]
        self.assertEqual(test.eval_stack(), -22)

    def test_sub_float(self):
        test = Application()
        test.inputstack = [1,2,'.',4,'-',3,4,'.',5]
        self.assertEqual(test.eval_stack(), -22.1)
    
    def test_mul(self):
        test = Application()
        test.inputstack = [1,2,'*',4]
        self.assertEqual(test.eval_stack(), 48)

    def test_mul_float(self):
        test = Application()
        test.inputstack = [1,'.',4,'*',3,'.',5]
        self.assertEqual(test.eval_stack(), 4.9)
    
    def test_div(self):
        test = Application()
        test.inputstack = [1,2,'/',4]
        self.assertEqual(test.eval_stack(), 3.0)

    def test_div_float(self):
        test = Application()
        test.inputstack = [1,'/',5]
        self.assertEqual(test.eval_stack(), 0.2)
