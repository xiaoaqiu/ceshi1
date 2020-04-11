import unittest
from moudle import Cal
import sys

class MoudleTest(unittest.TestCase):
    def setUp(self):
        self.cal=Cal(8,4)
    def tearDown(self):
        pass
    def test_add(self):
        result=self.cal.add()
        self.assertEqual(result,12)
    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)
    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(result,32)
    def test_div(self):
        result=self.cal.div()
        self.assertEqual(result,2)

if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(MoudleTest("test_add"))
    suite.addTest(MoudleTest("test_sub"))
    suite.addTest(MoudleTest("test_mul"))
    suite.addTest(MoudleTest("test_div"))
    with open('a.text','w') as report_file:
        runner=unittest.TextTestRunner(stream=report_file, verbosity=2)
        runner.run(suite)





