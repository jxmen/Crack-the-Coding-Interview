# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # bst의 root가 주어지면 key를 삭제하고 업데이트된 bst의 root를 리턴한다.
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node: Optional[TreeNode]):
            if node is None:
                return None

            if node.left is None:
                return node

            return find_min(node.left)

        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # core concept: 지우려고 하는 노드에서 오른쪽에서 가장 작은 값을 찾고, 그 값을 스왑하고 해당 값을 삭제 처리한다.
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_of_right = find_min(root.right)
        root.val = min_of_right.val
        root.right = self.deleteNode(root.right, root.val) # 바꾼 값을 다시 삭제처리 하기 위해 root.val을 넣어준다.

        return root


