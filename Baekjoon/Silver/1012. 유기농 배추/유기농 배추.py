import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(grid, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def visit(r, c):
        grid[r][c] = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                visit(nr, nc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                visit(r, c)
                count += 1

    return count


t = int(input())
for _ in range(t):
    cols, rows, k = map(int, input().split())
    grid = [[0] * cols for _ in range(rows)]

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1

    print(solution(grid, rows, cols))
