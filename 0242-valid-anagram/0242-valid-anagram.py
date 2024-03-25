class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s와 t를 비교해서 아나그램이면 true를 리턴하라.

        아나그램은 원래 문자를 하나씩만 사용하여 재배열 시 특정 단어가 되는 것을 말한다.
        """

        if s == t:
            return True

        if len(s) != len(t):
            return False

        # s와 t를 정렬하고, 모두 일치할 경우 True를 리턴한다.
        # O(n log n) * 2 = O(2n log n) = O(n log n)
        return sorted(s) == sorted(t)


from unittest import TestCase


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test(self):
        self.assertTrue(self.solution.isAnagram(s="anagram", t="nagaram"))

    def test2(self):
        self.assertFalse(self.solution.isAnagram(s="rat", t="car"))

    def test3(self):
        self.assertFalse(self.solution.isAnagram(s="a", t="ab"))

    def test4(self):
        self.assertTrue(self.solution.isAnagram(s="a", t="a"))
