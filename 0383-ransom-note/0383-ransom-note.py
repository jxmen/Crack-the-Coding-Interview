"""
r - m 했을 때 r이 아무것도 안남았다면 True, 아니면 False

Counter
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        return not (r - m)
