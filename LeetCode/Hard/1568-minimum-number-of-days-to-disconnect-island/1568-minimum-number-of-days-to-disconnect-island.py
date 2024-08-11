from collections import deque
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            queue = deque([(x, y)])
            visited[x][y] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                        continue

                    if not visited[nx][ny] and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

        def islandCount():
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        bfs(i, j)
                        count += 1
            return count

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        flattened = [item for sublist in grid for item in sublist]
        if flattened.count(1) == 0: return 0

        # 섬이 이미 끊어졌는지 확인한다. 그렇다면 0을 리턴한다.
        count = islandCount()
        if count >= 2:
            return 0

        # 만약 count가 1인데 나머지가 모두 0이라면, 외딴섬이다. 이 경우 바로 1을 리턴한다.
        if count == 1:
            flattened = [item for sublist in grid for item in sublist]
            if flattened.count(1) == 1:
                return 1

        # 하나만 지워도 되는 경우라면 1, 아닐 경우 2를 리턴한다.
        # 하나씩 지우고 섬의 개수를 체크한다. 섬의 개수가 모두 1이라면 2를 리턴한다.
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # 육지 한개를 0으로 바꾼다. 그 이후 섬이 2개 이상이면 1을 리턴한다.
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
                    if islandCount() >= 2:
                        return 1
                    grid[i][j] = 1

        # 그 외에 경우는 2를 리턴한다.
        return 2


