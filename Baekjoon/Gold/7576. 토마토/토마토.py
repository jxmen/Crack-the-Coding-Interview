from collections import deque
import sys

input = sys.stdin.readline



# 모두 0이라면 level을, 아니라면 -1 리턴
def solution(grid, rows, cols):
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                queue.append((i, j))

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    days = 0

    while queue:
        len_queue = len(queue)
        for _ in range(len_queue):
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    grid[nx][ny] = 1  # 방문 표시
                    queue.append((nx, ny))

        days += 1

    days = max(0, days - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                return -1

    return days

cols, rows = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

print(solution(grid, rows, cols))
