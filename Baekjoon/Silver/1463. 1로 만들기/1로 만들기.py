import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution_bottom_up(n):
    """
    bottom-up DP 기반 풀이.

    나누는 것이 아닌 2부터 시작하여 n이 될때까지 +, * 연산을 통해 횟수를 구한다.
    """
    dp = [0] * (n + 1)
    for i in range(2, n + 1):

        """
        +1 연산으로 먼저 초기화 후, 곱하기 연산이 더 적으면 갱신 
        """
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]


def solution_top_down(n, cache):
    if n in cache:
        return cache[n]

    min_count = solution_top_down(n - 1, cache) + 1
    if n % 3 == 0:
        min_count = min(min_count, solution_top_down(n // 3, cache) + 1)

    if n % 2 == 0:
        min_count = min(min_count, solution_top_down(n // 2, cache) + 1)

    cache[n] = min_count

    return cache[n]


n = int(input())
# cache = {1: 0}
print(solution_bottom_up(n))
