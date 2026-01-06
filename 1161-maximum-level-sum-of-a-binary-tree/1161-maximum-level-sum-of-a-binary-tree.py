# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        
        # bfs로 각 레벨별 합계 구하기
        dq = deque([root])
        while dq:
            dq_len = len(dq)
            level_sum = 0
            for _ in range(dq_len):
                popped = dq.popleft()
                level_sum += popped.val

                if popped.left:
                    dq.append(popped.left)
                if popped.right:
                    dq.append(popped.right)
            
            sums.append(level_sum)

        # 최대 레벨 값 구하기
        return sums.index(max(sums)) + 1
