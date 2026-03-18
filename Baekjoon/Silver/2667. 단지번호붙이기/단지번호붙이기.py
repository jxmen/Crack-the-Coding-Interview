import sys
input = sys.stdin.readline

n = int(input())
grid = [[None] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    s = input()
    for j in range(n):
        grid[i][j] = int(s[j])


def visit(grid, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    count = 1  # 현재 셀 포함

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
            count += visit(grid, nx, ny)

    return count

# grid를 전체 순회하면서 visit 처리한다. 그리고 단지내 집의 개수도 구한다.
answer = 0
house_counts = []
for i in range(n):
    for j in range(n):
        # grid
        if not visited[i][j] and grid[i][j] == 1:
            answer += 1
            house_count = visit(grid, i, j)
            house_counts.append(house_count)

# --- print
house_counts.sort()
print(answer)
for house_count in house_counts:
    print(house_count)

