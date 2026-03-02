"""
"aba" -> "aa" -> true
"abca" -> "aca" -> true

TODO:
time limit exceed -> 효율적으로 풀 수 있는 방법이 없을까?
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            return s == s[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (is_palindrome(s[left:right])
                        or is_palindrome(s[left + 1:right + 1]))

            left, right = left + 1, right - 1

        return True
