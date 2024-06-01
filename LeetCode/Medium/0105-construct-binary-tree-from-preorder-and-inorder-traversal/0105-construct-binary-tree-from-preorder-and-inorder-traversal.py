# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 중위순회와 전위순회로 구성된 배열이 주어일 때, 트리를 생성해서 리턴하라.
        if len(inorder) == 0:
            return None
        
        
        # preorder[0] 값이 inorder array 기준에서는 왼쪽은 왼쪽 트리, 오른쪽은 오른쪽 자식 트리가 된다.
        # preorder = [3, 5], inorder = [5, 3] 일때 prorder[0]인 3이 root가 되고 inorder에서는 3 왼쪽에 있는 [5]가 3의 왼쪽 서브트리가 된다.
        
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root
        
        
        