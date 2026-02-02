# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def get_values(root):
            if not root:
                return []

            v = []
            if root.left:
                v.extend(get_values(root.left))

            v.append(root.val)
            if root.right:
                v.extend(get_values(root.right))

            return v

        # get_values를 깔끔하게 바꾼 버전
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i-1])
        return min_diff
