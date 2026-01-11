class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 큐를 안써도 되지 않나?
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1
