# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # 1. 최대값을 찾고 이를 루트로 만든다.
        max_of_nums = max(nums)
        root = TreeNode(max_of_nums)
        
        # 2. array에서 root보다 왼쪽에 있는 것들은 root 왼쪽에 위치시킨다.
        leftMax = self.constructMaximumBinaryTree(nums[:nums.index(max_of_nums)])
        root.left = leftMax
        
        rightMax = self.constructMaximumBinaryTree(nums[nums.index(max_of_nums)+1:])
        root.right = rightMax
        
        return root
