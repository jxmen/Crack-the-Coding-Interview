from unittest import TestCase


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        외부 괄호 제거

        바깥에 감싸져 있는 괄호를 제거하고 모두 더한 괄호 문자열을 리턴하라.
        감싸져 있지 않다면 빈 문자열을 리턴해야 한다.

        :param s: 괄호 문자열. 올바른 값만 주어진다. 1 <= s.length <= 10^5
        :return: 외부 괄호를 제거한 문자열. e.g) (()) -> ()
        """

        stack = []
        result = ""

        for c in list(s):
            if c == '(':
                if stack:
                    result += '('
                stack.append(c)
                continue

            stack.pop()
            if stack:
                result += ')'

        return result


class Test(TestCase):

    @classmethod
    def setUpClass(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.removeOuterParentheses("()()"), "")

    def test2(self):
        self.assertEqual(self.sol.removeOuterParentheses("((()))"), "(())")
