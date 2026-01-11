class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 큐를 안써도 되지 않나?
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        
        return -1
