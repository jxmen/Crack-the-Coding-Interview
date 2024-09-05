# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(r, depth = 1):
            if not r: return depth

            return max(getDepth(r.left, depth + 1), getDepth(r.right, depth + 1))

        if not root: return 0

        return max(getDepth(root.left), getDepth(root.right))

    