# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cache = {}

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        pathSums = []

        # 모든 노드를 돌면서, 자신이 포함된 경로의 최대 합계를 구한다.
        while len(queue):
            queueLen = len(queue)
            for i in range(queueLen):
                node = queue.popleft()
                left = self.maxPathSumFrom(node.left)
                right = self.maxPathSumFrom(node.right)

                # 현재 노드를 포함한 값 중 경로의 최대값을 추가한다.
                currentNodeMaxPathSum = max(
                    node.val,
                    node.val + left,
                    node.val + right,
                    (node.val + left + right)
                )
                pathSums.append(currentNodeMaxPathSum)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max(pathSums)

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
