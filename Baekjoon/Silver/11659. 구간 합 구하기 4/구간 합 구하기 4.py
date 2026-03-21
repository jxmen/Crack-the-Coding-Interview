import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = p[i-1] + arr[i-1]

for _ in range(m):
    l, r = map(int, input().split())
    result = p[r] - p[l-1]
    print(result)
