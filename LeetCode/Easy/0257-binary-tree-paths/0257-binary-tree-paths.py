# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]

        paths = []
        if root.left:
            for l in self.binaryTreePaths(root.left):
                s = str(root.val)
                s += '->'
                s += l
                paths.append(s)
        
        if root.right:
            for r in self.binaryTreePaths(root.right):
                s = str(root.val)
                s += '->'
                s += r
                paths.append(s)

        return paths
    
