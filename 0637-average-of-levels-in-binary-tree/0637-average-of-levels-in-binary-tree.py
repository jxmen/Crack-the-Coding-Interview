# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        averages = []
        queue = deque([root])
        while queue:
            queue_length = len(queue)
            nodes = []
            for _ in range(queue_length):
                node = queue.popleft()
                nodes.append(node)

                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None

            averages.append(sum(node.val for node in nodes) / queue_length)

        return averages
