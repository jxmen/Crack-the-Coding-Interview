import sys

input = sys.stdin.readline


def solution(arr, n, m):
    l, r = 0, 0

    s = arr[0]
    c = 0
    while r < n and l < n:
        if s == m:
            c += 1

            s -= arr[l]
            l += 1
        elif s > m:
            s -= arr[l]
            l += 1
        else:
            r += 1
            if r < n:
                s += arr[r]

    return c



n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(arr, n, m))
