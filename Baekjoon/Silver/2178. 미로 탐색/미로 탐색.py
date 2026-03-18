import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

for i in range(n):
    s = input()
    for j in range(m):
        grid[i][j] = s[j]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(grid, n, m):
    count = 1
    queue = deque([(0, 0)])
    grid[0][0] = '0'
    while queue:
        queue_len = len(queue)
        for _ in range(queue_len):
            x, y = queue.popleft()
            if x == n - 1 and y == m - 1:
                return count

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))

        count += 1

    return None


print(solution(grid, n, m))
