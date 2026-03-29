import sys

input = sys.stdin.readline


def solution(n, arr, x):
    cnt = 0
    a = sorted(arr)

    left, right = 0, n - 1
    while left < right:
        total = a[left] + a[right]
        if total == x:
            cnt += 1
            right -= 1
        elif total > x:
            right -= 1
        else:
            left += 1

    return cnt


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(solution(n, arr, x))
