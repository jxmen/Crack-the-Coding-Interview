# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # root부터 t에 해당하는 경로의 개수를 리턴한다.
        def helper(r, t): 
            if not r: return 0

            paths = 0
            if r.val == t:
                paths += 1
            
            paths += helper(r.left, t-r.val)
            paths += helper(r.right, t-r.val)

            return paths
        
        paths = helper(root, targetSum)
        if root:
            paths += self.pathSum(root.left, targetSum)
            paths += self.pathSum(root.right, targetSum)

        return paths
        