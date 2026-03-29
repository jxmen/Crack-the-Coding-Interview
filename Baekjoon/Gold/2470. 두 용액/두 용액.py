import sys

input = sys.stdin.readline


def solution(arr):
    arr.sort()
    left, right = 0, len(arr) - 1

    ans = [arr[left], arr[right]]
    while left < right:
        total = arr[left] + arr[right]
        if abs(total) < abs(sum(ans)):
            ans = [arr[left], arr[right]]

        if total >= 0:
            right -= 1
        else:
            left += 1

    return ans


n = int(input())
arr = list(map(int, input().split()))

print(' '.join(map(str, solution(arr))))
