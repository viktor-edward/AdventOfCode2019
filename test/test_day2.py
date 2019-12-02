import unittest
from src import day2


class TestDay2(unittest.TestCase):

    def test_case1(self):
        output = day2.updateOpcodes([1, 0, 0, 0, 99])
        correctOutput = [2, 0, 0, 0, 99]
        self.assertEqual(correctOutput, output,
                         msg="Output should be" + str(correctOutput))

    def test_case2(self):
        output = day2.updateOpcodes([2, 3, 0, 3, 99])
        correctOutput = [2, 3, 0, 6, 99]
        self.assertEqual(correctOutput, output,
                         msg="Output should be" + str(correctOutput))

    def test_case3(self):
        output = day2.updateOpcodes([1, 1, 1, 4, 99, 5, 6, 0, 99])
        correctOutput = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(correctOutput, output,
                         msg="Output should be" + str(correctOutput))
