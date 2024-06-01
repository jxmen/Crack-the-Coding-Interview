# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # only root-leaf path
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, total = 0) -> bool:
        if root is None:
            return False

        if total + root.val == targetSum and root.left == None and root.right == None:
            return True
        
        leftHasSum = self.hasPathSumHelper(root.left, targetSum, root.val)
        rightHasSum = self.hasPathSumHelper(root.right, targetSum, root.val)
        return leftHasSum or rightHasSum
    
    def hasPathSumHelper(self, root: Optional[TreeNode], targetSum: int, total: int) -> bool:
        if root is None:
            return False
        
        if total + root.val == targetSum and root.left == None and root.right == None:
            return True
        
        leftHasSum = self.hasPathSumHelper(root.left, targetSum, total + root.val)
        rightHasSum = self.hasPathSumHelper(root.right, targetSum, total + root.val)
        return leftHasSum or rightHasSum
        