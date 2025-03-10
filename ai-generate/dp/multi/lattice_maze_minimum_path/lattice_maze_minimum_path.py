"""

목표: (n-1, m-1) 까지 이동하기 위한 최소 좌표를 구하려 한다.
- 그렇다면, (n-2, m-1)과 (n-1, m-2) 좌표 중 더 작은 것으로 이동 후, (n-1, m-1)로 이동하면 된다.
- 둘 중에 작은 것이 있다면 그 좌표에서 또 상하좌우로 이동하기 전 가장 작은 최소값으로 먼저 이동하면 된다.


3 4
1 3 5 2
3 8 1 4
5 2 7 3

dp 테이블
0 0 0 0
0 0 0 0
0 0 0 0

dp[0][0] = table[0][0]

이제 오른쪽과 아래로 이동하면서, 이동하기 위한 최소값을 dp 테이블에 없데이트한다.

for i in range(n):
    for j in range(m):
        # 오른쪽으로 이동 (테이블을 벗어나지 않았다면)
        # m이 4일때, j는 m-1, 즉 3보다 크면 안된다
        if j < m-2:
            dp[i][j+1] = table[i][j+1] + dp[i][j]

        # 아래로 이동
        # n이 3이라면, i는 n-1보다 크면 안된다
        if i < n-2:
            dp[i+1][j] = table[i+1][j] + dp[i][j]


print(dp[n-1][m-1])

"""

n, m = map(int, input().split())
table = []

for i in range(n):
    table.append(list(map(int, input().split())))

dp = [[0] * (m) for _ in range(n)]

dp[0][0] = table[0][0]

# 첫번째 행 초기화
for j in range(1, m):
    dp[0][j] = table[0][j] + dp[0][j-1]

# 첫번째 열 초기화
for i in range(1, n):
    dp[i][0] = table[i][0] + dp[i-1][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + table[i][j]

print(dp[n - 1][m - 1])
