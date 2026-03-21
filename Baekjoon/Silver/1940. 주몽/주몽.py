import sys

input = sys.stdin.readline


def solution(arr, n, m):
    a = sorted(arr)

    count = 0
    l, r = 0, n - 1

    while l < r:
        if a[l] + a[r] == m:
            count += 1
            l += 1
            r -= 1
        elif a[l] + a[r] > m:
            r -= 1
        else:
            l += 1

    return count


n = int(input())
m = int(input())
arr = list(map(int, input().split()))

print(solution(arr, n, m))
