import sys

input = sys.stdin.readline

n = int(input())
c = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[i][0] = r, [i][1] = g, [i][2] = b
dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = c[0][0]
dp[0][1] = c[0][1]
dp[0][2] = c[0][2]

for i in range(1, n):
    r, g, b, = c[i]

    # 레드로 칠하는 경우 - 이전에 레드가 아닌 것중 최소 값에서 지금 레드값 더하기
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r

    # 그린 - (레드 or 블루) -> 그린
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g

    # 파랑
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b

print(min(dp[n - 1]))
