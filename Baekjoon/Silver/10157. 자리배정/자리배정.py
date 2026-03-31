import sys

input = sys.stdin.readline


def solution(cols, rows, k):
    if k > cols * rows:
        return '0'

    grid = [[0] * cols for _ in range(rows)]

    x, y = rows - 1, 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0
    number = 1
    while grid[x][y] == 0:
        grid[x][y] = number
        if number == k:
            return f"{y + 1} {rows - x}"

        number += 1
        nx, ny = x + directions[di][0], y + directions[di][1]
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            x, y = nx, ny
        else:
            di = (di + 1) % len(directions)
            x, y = x + directions[di][0], y + directions[di][1]
          
    return None


if __name__ == '__main__':
    c, r = map(int, input().split())
    k = int(input())

    print(solution(c, r, k))
