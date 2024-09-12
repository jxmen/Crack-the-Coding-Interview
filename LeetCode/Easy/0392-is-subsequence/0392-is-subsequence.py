class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == len(t) == 0:
            return True

        if len(t) == 0:
            return False

        p2 = 0
        for p1 in range(len(s)):
            while p2 < len(t) and s[p1] != t[p2]:
                p2 += 1

            if p2 == len(t):
                return False
            
            p2 += 1
        
        return True
