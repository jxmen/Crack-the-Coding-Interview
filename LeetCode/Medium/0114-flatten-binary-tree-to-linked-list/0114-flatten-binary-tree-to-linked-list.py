# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
중위 순회로 트리를 linked list로 만들기

    1
   /
  2
 / \
3   4

    1
   /
  2
   \
    3
     \
      4

중위 순회를 잘 이용해보자.
중위 순회란? - 자신-왼쪽-오른쪽 순으로 순회
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        elif not root.left and not root.right:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        if root.left and root.right:
            tmpRootRight = root.right
            
            # 원래 오른쪽이였던 노드를 재배치한 노드 오른쪽에 붙인다.
            root.right = root.left
            self.attach(root.right, tmpRootRight)
            root.left = None
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
    
    def attach(self, root: Optional[TreeNode], target: Optional[TreeNode]) -> None:
        if root.right is None:
            root.right = target
            root.left = None
            return

        self.attach(root.right, target)
