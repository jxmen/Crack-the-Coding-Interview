import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-indexed

p = [0] * (n + 1)  # 1-indexed
for i in range(1, n + 1):
    p[i] = p[i - 1] + arr[i]

# 연속 k일 중에서 최대값 찾기
l, r = 0, k
max_prefix = p[k] - p[0]
while r < (n + 1):
    max_prefix = max(max_prefix, p[r] - p[l])
    l += 1
    r += 1

print(max_prefix)
