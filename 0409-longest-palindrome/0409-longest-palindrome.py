from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        result = 0
        has_odd = False

        for count in freq.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                has_odd = True

        return result + (1 if has_odd else 0)
