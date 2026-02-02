class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert, delete, replace: 상태 3개
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case: 빈 문자열에서 변환
        for i in range(n + 1):
            dp[i][0] = i  # word1[:i] → "" : i번 삭제
        for j in range(m + 1):
            dp[0][j] = j  # "" → word2[:j] : j번 삽입

        # dp[i][j] = w1[0...i]가 w2[0...j]가 되기 위한 최소 연산 횟수
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[n][m]
