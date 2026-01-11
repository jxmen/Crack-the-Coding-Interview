from collections import deque

class Solution:

    # 큐로 구현하기
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        dq = deque()
        for i, c in enumerate(s):
            dq.append((c, i)) # 인덱스도 저장
            
            while dq and count[dq[0][0]] > 1:
                dq.popleft()
            
        return dq[0][1] if dq else -1

    def firstUniqChar2(self, s: str) -> int:
        # 큐를 안써도 되지 않나?
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1
