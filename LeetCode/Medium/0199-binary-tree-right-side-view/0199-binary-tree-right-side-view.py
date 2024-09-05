# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        queue = deque([root])
        views = []

        while queue:
            # 큐를 size 개수만큼 값을 꺼낸다.
            qlen = len(queue)
            for i in range(qlen):
                p = queue.popleft()
                # 맨 처음 꺼낸 값만 views에 값을 추가한다. (오른쪽부터 큐에서 빼오기 때문)
                if i == 0:
                    views.append(p.val)

                # 큐에서 꺼낸 값이 오른쪽 자식이 있는지 체크하고, 오른쪽을 먼저 큐에 먼저 넣는다.
                if p.right:
                    queue.append(p.right)

                # 왼쪽 자식도 있다면 왼쪽도 넣는다.
                if p.left:
                    queue.append(p.left)

        return views
            
        
        
