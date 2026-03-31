import sys

input = sys.stdin.readline


def solution(n, m, grid1, grid2):
    result = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(grid1[i][j] + grid2[i][j])

        result.append(row)

    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    grid1 = [list(map(int, input().split())) for _ in range(n)]
    grid2 = [list(map(int, input().split())) for _ in range(n)]

    result = solution(n, m, grid1, grid2)
    for row in result:
        print(' '.join(map(str, row)))
