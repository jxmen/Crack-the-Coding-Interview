import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]
# n*n 입력받기

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        arr[i+1][j+1] = nums[j]

p = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        p[i][j] = arr[i][j] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = p[x2][y2] - p[x1-1][y2] - p[x2][y1-1] + p[x1-1][y1-1]
    print(result)

