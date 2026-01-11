# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max(self, node):
        while node.right:
            node = node.right
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 찾을 키로 이동
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # 자식이 없는 경우
        if not root.left and not root.right:
            return None

        # 자식이 하나인 경우
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # === 자식이 둘 다 있는 경우 ===
        # (항상 한쪽만 사용한다 — 여기서는 왼쪽 최대)
        predecessor = self.find_max(root.left)

        root.val = predecessor.val
        root.left = self.deleteNode(root.left, predecessor.val)
            
        return root