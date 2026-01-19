class Solution:

    # 이익이 0보다 클 경우 최대값 - 최소값
    def maxProfit(self, prices: List[int]) -> int:
        non = 0
        take = prices[0]
        for i in range(1, len(prices)):
            # 점화식을 먼저 세우자
            price = prices[i]

            non = max(non, price - take)
            take = min(take, price)
        
        return non

