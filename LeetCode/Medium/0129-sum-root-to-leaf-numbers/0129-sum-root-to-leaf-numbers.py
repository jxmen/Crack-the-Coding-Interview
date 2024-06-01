# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
        
        if root.left is None:
            return self.getTotal(root.right, root.val)
        elif root.right is None:
            return self.getTotal(root.left, root.val)
        else:
            left = self.getTotal(root.left, root.val)
            right = self.getTotal(root.right, root.val)
            return left + right
    
    def getTotal(self, root: Optional[TreeNode], prefix: int) -> int:
        if root is None:
            return prefix
        
        if root.left is None and root.right is None:
            return int(str(prefix) + str(root.val))
        
        newPrefix = int(str(prefix) + str(root.val)) 
        if root.left is None:
            return self.getTotal(root.right, newPrefix)
        elif root.right is None:
            return self.getTotal(root.left, newPrefix)
        
        return self.getTotal(root.left, newPrefix) + self.getTotal(root.right, newPrefix)
    