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
        
        # bfs로 각 레벨별 합계를 최대값과 비교하고 갱신
        dq = deque([root])
        current_level = 1
        max_sum, max_level = root.val, 1
        while dq:
            dq_len = len(dq)
            current_level_sum = 0
            for _ in range(dq_len):
                node = dq.popleft()
                current_level_sum += node.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            # 최대값 갱신
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
            
            current_level += 1
        
        return max_level


    def maxLevelSum2(self, root: Optional[TreeNode]) -> int:
        sums = []
        
        # bfs로 각 레벨별 합계 구하기
        dq = deque([root])
        while dq:
            dq_len = len(dq)
            current_level_sum = 0
            for _ in range(dq_len):
                node = dq.popleft()
                current_level_sum += node.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            sums.append(current_level_sum)

        # 최대 레벨 값 구하기
        return sums.index(max(sums)) + 1


   