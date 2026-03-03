from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        n, m = len(mat), len(mat[0])
        v = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    v[i][j] = True

        level = 0
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                i, j = queue.popleft()
                mat[i][j] = level

                # 상하좌우 값 큐에 넣기
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and not v[ni][nj]:
                        v[ni][nj] = True
                        queue.append((ni, nj))

            level += 1

        return mat
