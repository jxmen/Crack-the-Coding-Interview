import sys
import copy

from itertools import combinations

input = sys.stdin.readline

def solution(grid, combo):
    def visit(x, y):
        grid[x][y] = 2
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                visit(nx, ny)

    def get_zero_count():
        zero_count = 0
        for row in grid:
            for cell in row:
                if cell == 0:
                    zero_count += 1

        return zero_count

    grid = copy.deepcopy(grid)
    for x, y in combo:
        grid[x][y] = 1

    # 전염 로직
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                visit(i, j)

    return get_zero_count()


# 세로 크기 N, 가로 크기 M
rows, cols = map(int, input().split())
grid = [
    list(map(int, input().split())) for _ in range(rows)
]

zeros = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            zeros.append((i, j))

max_count = 0
for combo in combinations(zeros, 3):
    max_count = max(max_count, solution(grid, combo))

print(max_count)
