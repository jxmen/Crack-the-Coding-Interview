import sys

input = sys.stdin.readline


def solution(arr, n, m):
    count = 0
    l = 0
    s = 0

    for r in range(n):
        s += arr[r]
        while s > m and l <= r:
            s -= arr[l]
            l += 1
        if s == m:
            count += 1

    return count



n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(arr, n, m))
