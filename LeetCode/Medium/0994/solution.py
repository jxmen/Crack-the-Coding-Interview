from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 처음 돌 좌표를 찾는다. (썩은 과일)
        n, m = len(grid), len(grid[0])
        fresh = 0
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])

                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        if len(queue) == 0:
            return -1

        level = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # 상하좌우를 이동한다. (dx 활용)
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                # dx, dy 이동한 값이 좌표를 벗어나지 않고 fresh(1)이라면 queue에 넣는다.
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        queue.append([nx, ny])
                        grid[nx][ny] = 2 # queue에 있는 값이 검사할 때 다시 넣지 않도록 미리 세팅

            if len(queue) == 0:
                break

            level += 1

        # 1이 아직 남아있다면 -1, 아니라면 level 리턴
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return level

