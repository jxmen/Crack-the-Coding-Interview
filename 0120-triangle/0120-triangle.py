class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')] * i for i in range(1, len(triangle)+1)]
        dp[0][0] = triangle[0][0]

        for i in range(len(triangle)-1):
            for j in range(len(triangle[i])):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + triangle[i+1][j]) # 왼쪽
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1]) # 오른쪽

        return min(dp[-1])