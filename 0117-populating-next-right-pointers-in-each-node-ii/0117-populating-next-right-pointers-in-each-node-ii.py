"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                p = queue.popleft()

                # 큐 마지막 요소가 아니라면, 큐에 있는 것을 next로 연결
                p.next = queue[0] if i < len_queue-1 else None

                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)

        return root
