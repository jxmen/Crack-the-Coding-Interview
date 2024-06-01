# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, maxLevel = 1, 1
        maxValue = root.val

        queue = deque([root])
        while len(queue):
            queueLen = len(queue)
            levelSum = 0
            for i in range(queueLen):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                
                levelSum += popped.val
                
            if levelSum > maxValue:
                maxValue = levelSum
                maxLevel = level
            
            level += 1
        
        return maxLevel
        