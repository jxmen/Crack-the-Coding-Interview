# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1 # 루트 포함
        dq = deque([root])
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                p = dq.popleft()
                if not p.left and not p.right:
                    return depth
                
                if p.left:
                    dq.append(p.left)
                if p.right:
                    dq.append(p.right)
            
            depth += 1
        
        return depth
