# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # root1과 root2의 마지막 자식 노드들을 모두 찾고 일치하면 true를 리턴한다.
        root1Leafs = self.getLeafs(root1)
        root2Leafs = self.getLeafs(root2)
        if len(root1Leafs) != len(root2Leafs):
            return False

        for root1Leaf, root2Leaf in zip(root1Leafs, root2Leafs):
            if root1Leaf.val != root2Leaf.val:
                return False

        return True

    def getLeafs(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root]

        leafs = []
        leafs.extend(self.getLeafs(root.left))
        leafs.extend(self.getLeafs(root.right))

        return leafs
