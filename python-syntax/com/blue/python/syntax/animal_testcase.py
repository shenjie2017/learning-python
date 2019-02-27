import unittest

from com.blue.python.syntax.dog import Dog
from com.blue.python.syntax.golden import Golden


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.golden = Golden("hua", 19)
        self.dog = Dog("huang", 12)

    def test_sit(self):
        self.golden.sit()
        self.dog.sit()

    def test_hello(self):
        self.golden.hello()
        self.dog.hello()

    def test_get_type(self):
        self.assertEqual(self.golden.get_type(),"hua golden")
        self.assertEqual(self.dog.get_type(),"huang dog")


if __name__ == '__main__':
    unittest.main()
