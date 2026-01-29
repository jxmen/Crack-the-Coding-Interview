"""
HashMap + counter
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(list(s))
        
        for c in list(t):
            if c not in s_map:
                return False
            else:
                s_map[c] -= 1
        
        return all(num == 0 for num in list(s_map.values()))
