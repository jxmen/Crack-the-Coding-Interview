class Solution:

    # 그리디로 풀기 - 상승할때 무조건 판다
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit

    # 변수 2개로 최적화 - 이전 상태 값만 사용하므로
    def maxProfit2(self, prices: List[int]) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            cash = max(cash, hold + price)
            hold = max(hold, cash - price)
        
        return cash
        
    # 첫 풀이 - 2차원 DP
    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][1] = -prices[0]

        # dp[i][0] = i날 안가지때 최대 이익
        # dp[i][1] = i날 가질 때 최대 이익

        for i in range(1, n):
            price = prices[i]

            # 안가질때 - 어제도 안가짐, 오늘 팜
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price)

            # 가질때 - 어제도 가짐, 오늘 삼
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - price)
        
        return dp[n-1][0]
        