import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]


def solution(arr, n):
    if n == 1:
        return arr[0]

    # dp[i][0] = 직전칸 밟음, [i][1] = 직전칸 안밟음
    dp = [[0, 0] for _ in range(n)]
    dp[0][0], dp[0][1] = arr[0], arr[0]
    dp[1][0], dp[1][1] = arr[0] + arr[1], arr[1]

    for i in range(2, n):
        dp[i][0] = dp[i - 1][1] + arr[i]
        dp[i][1] = max(dp[i - 2]) + arr[i]

    return max(dp[n - 1])


print(solution(numbers, n))
