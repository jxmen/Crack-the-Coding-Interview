from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 모두 0이라면 level을, 아니라면 -1 리턴
def solution(grid, n, m):
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))

    level = 0
    while queue:
        len_queue = len(queue)
        for _ in range(len_queue):
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1  # 방문 표시
                    queue.append((nx, ny))

        if queue:
            level += 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                return -1

    return level


print(solution(grid, n, m))
