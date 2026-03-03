from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 기존 문자에서 이미 존재하는 문자가 있다면, 해당 문자까지 잘라내고 더한다.
        # abc 에서 'b' 추가시 -> ab를 잘라내고 b를 추가 -> 'cb'
        # 문자의 set을 만들고, 문자 삭제/추가 할때마다 set의 값도 업데이트 해준다.
        char_set = set()
        queue = deque()
        max_len = 0
        
        for c in list(s):
            if c not in char_set:
                queue.append(c)
                char_set.add(c)
            else:
                while queue[0] != c:
                    char_set.remove(queue.popleft())
                
                queue.popleft()
                queue.append(c)
            
            max_len = max(max_len, len(queue))

        return max_len