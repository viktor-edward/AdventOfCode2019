import unittest
from src import day1


class TestFxQuoteGenerator(unittest.TestCase):

    def test_helloWorldFunc(self):
        outputString = day1.helloWorld()
        self.assertEqual(outputString, "Hello World!",
                         msg="Output should be  \"Hello World!\"")
