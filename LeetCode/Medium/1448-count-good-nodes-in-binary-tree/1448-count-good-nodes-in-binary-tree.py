# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        leftCount = self.goodNodesHelp(root.left, root.val)
        rightCount = self.goodNodesHelp(root.right, root.val)

        # 자신과 왼쪽 + 오른쪽 자식의 good node 개수를 리턴한다. 
        return leftCount + rightCount + 1 # root는 무조건 good node이므로 + 1 해준다.
    
    def goodNodesHelp(self, head: TreeNode, maxValue: int) -> int:
        if not head:
            return 0

        if head.val >= maxValue:
            left = self.goodNodesHelp(head.left, head.val)
            right = self.goodNodesHelp(head.right, head.val)
            return 1 + left + right # 자신은 good node로 count하여 +1 해준다.
        else:
            left = self.goodNodesHelp(head.left, maxValue)
            right = self.goodNodesHelp(head.right, maxValue)
            return left + right