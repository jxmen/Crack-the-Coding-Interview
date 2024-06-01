# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = 1
        levelSums = []

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
            
            levelSums.append(levelSum)
            level += 1
        
        if k > len(levelSums):
            return -1

        return sorted(levelSums, reverse=True)[k-1]
