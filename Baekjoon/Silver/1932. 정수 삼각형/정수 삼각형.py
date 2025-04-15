"""
점화식

current = arr[i][j]
dp[i][j] = max(dp[i][j], dp[i-1][j-1] + current, dp[i-1][j] + current))

"""


def solution(arr):
    n = len(arr)
    dp = []
    for i in range(1, n + 1):
        dp.append([0] * i)

    dp[0][0] = arr[0][0]
    for i in range(1, n):
        current_nums = arr[i]
        for j in range(len(current_nums)):
            current_num = current_nums[j]
            if j == 0:  # 맨 왼쪽
                dp[i][j] = dp[i - 1][j] + current_num
            elif j == len(arr[i]) - 1:  # 맨 오른쪽
                dp[i][j] = dp[i - 1][j - 1] + current_num
            else:
                dp[i][j] = max(
                    dp[i - 1][j - 1] + current_num,
                    dp[i - 1][j] + current_num
                )

    return max(dp[n - 1])


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        nums = list(map(int, input().split()))
        arr.append(nums)

    print(solution(arr))
