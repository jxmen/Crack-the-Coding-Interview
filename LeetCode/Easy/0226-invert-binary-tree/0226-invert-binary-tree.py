# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 왼쪽을 오른쪽으로, 오른쪽을 왼쪽으로
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        root_left = root.left
        
        root.left = root.right
        root.right = root_left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        