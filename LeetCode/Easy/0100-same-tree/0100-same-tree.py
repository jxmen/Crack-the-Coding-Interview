# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        # p와 q와 왼쪽과 오른쪽이 모두 같다면 true를 리턴
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        