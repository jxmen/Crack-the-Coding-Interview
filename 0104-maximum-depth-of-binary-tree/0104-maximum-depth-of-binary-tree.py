# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 왼쪽 자식과 오른쪽 자식에서 높이를 구한 후, 둘의 max값 리턴
        def helper(root, depth):
            if not root:
                return depth

            left = helper(root.left, depth + 1)
            right = helper(root.right, depth + 1)

            return max(left, right)

        return helper(root, 0)
