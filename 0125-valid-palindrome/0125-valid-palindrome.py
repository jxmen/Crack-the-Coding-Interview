class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        for i in range(n // 2):
            start, end = s[i], s[n - i - 1]
            if start != end:
                return False

        return True
