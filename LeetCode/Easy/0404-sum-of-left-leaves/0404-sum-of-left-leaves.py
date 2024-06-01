# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return self.sumLeft(root.left) + self.sumRight(root.right)
        
    
    def sumLeft(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val
        
        return self.sumLeft(root.left) + self.sumRight(root.right)
        
    def sumRight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0
        
        return self.sumLeft(root.left) + self.sumRight(root.right)
