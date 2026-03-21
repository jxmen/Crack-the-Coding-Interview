import sys

input = sys.stdin.readline


def solution(arr, n, m):
    min_len = float('inf')
    l = 0
    s = 0

    for r in range(n):
        s += arr[r]
        while s >= m and l <= r:
            min_len = min(min_len, (r - l + 1))
            s -= arr[l]
            l += 1

    return min_len if min_len != float('inf') else 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(arr, n, m))
