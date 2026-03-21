import sys

from itertools import combinations

input = sys.stdin.readline

def solution(grid, combo, viruses, rows, cols):
    def visit(x, y):
        grid[x][y] = 2
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                visit(nx, ny)

    grid = [row[:] for row in grid]
    for x, y in combo:
        grid[x][y] = 1

    # 전염 로직 (bfs)
    for i, j in viruses:
        visit(i, j)

    return sum(cell == 0 for row in grid for cell in row)


# 세로 크기 N, 가로 크기 M
rows, cols = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(rows)
]

zeros, viruses = [], []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            zeros.append((i, j))
        elif grid[i][j] == 2:
            viruses.append((i, j))

max_count = 0
for combo in combinations(zeros, 3):
    max_count = max(max_count, solution(grid, combo, viruses, rows, cols))

print(max_count)
