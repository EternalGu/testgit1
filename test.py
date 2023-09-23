import unittest
from testgit1.urok2 import adder


class MyTest(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)

    def test_mixed(self):
        self.assertEqual(adder(2, a=4), 6)

    def test_dif(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, a=x), 5)

    def test_wrong(self):
        self.assertEqual(adder('2', 'abc', 10), 12)




if __name__ == '__main__':
    unittest.main()
