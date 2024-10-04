from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {1: {'nums': [3, 2, 3], 'output': 3},
                            2: {'nums': [2, 2, 1, 1, 1, 2, 2], 'output': 2}}
        self.__obj = Solution()
        return super().setUp()
    
    def test_Case1(self):
        nums, output = self.__testCases[1].values()
        result = self.__obj.majorityElement(nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    def test_Case2(self):
        nums, output = self.__testCases[2].values()
        result = self.__obj.majorityElement(nums)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()