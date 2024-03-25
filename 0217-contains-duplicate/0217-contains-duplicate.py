from typing import List
from unittest import TestCase


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        정수 array nums가 주어질 때, true를 리턴해라 만약 어떤 값이 두 번 이상 나타나면.
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)

        return False


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test2(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test3(self):
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
