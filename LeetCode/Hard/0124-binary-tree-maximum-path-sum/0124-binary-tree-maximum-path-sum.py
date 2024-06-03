# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cache = {}


    # TODO: bottom-up 방식으로 풀어보기
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        # 모든 노드를 돌면서, 자신이 포함된 경로의 최대 합계를 구한다.
        left = self.maxPathSumFrom(root.left)
        right = self.maxPathSumFrom(root.right)

        # 현재 노드를 포함한 값 중 경로의 최대값을 추가한다.
        maxPathSum = max(
            root.val,
            root.val + left,
            root.val + right,
            (root.val + left + right)
        )

        leftMaxPathSum = self.maxPathSum(root.left)
        rightMaxPathSum = self.maxPathSum(root.right)
        if leftMaxPathSum is None and rightMaxPathSum is None:
            return maxPathSum
        elif leftMaxPathSum is None:
            return max(maxPathSum, rightMaxPathSum)
        elif rightMaxPathSum is None:
            return max(maxPathSum, leftMaxPathSum)
        else:
            return max(maxPathSum, leftMaxPathSum, rightMaxPathSum)

    # root를 포함한 경로의 최대값을 리턴한다.
    def maxPathSumFrom(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root in self.cache:
            return self.cache[root]

        if not root.left and not root.right:
            return root.val

        if not root.right:
            left = self.maxPathSumFrom(root.left)
            return max(root.val, (root.val + left))

        if not root.left:
            right = self.maxPathSumFrom(root.right)
            return max(root.val, (root.val + right))

        left = self.maxPathSumFrom(root.left)
        right = self.maxPathSumFrom(root.right)

        pathSum = max(root.val, root.val + left, root.val + right)
        self.cache[root] = pathSum
        return pathSum
