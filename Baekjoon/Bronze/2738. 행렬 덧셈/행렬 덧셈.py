def solution(a, b):
    n, m = len(a), len(a[0])
    result = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[i][j] = a[i][j] + b[i][j]

    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    result = solution(a, b)
    for i in range(n):
        for j in range(m):
            print(result[i][j], end=' ')
        print()
