# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(r, t, vlist):
            if not r: return []
            paths = []

            vlist.append(r.val)
            if not r.left and not r.right and r.val == t:
                paths.append(list(vlist))
            
            paths += helper(r.left, t-r.val, vlist)
            paths += helper(r.right, t-r.val, vlist)

            vlist.pop()

            return paths
            
        return helper(root, targetSum, [])
        