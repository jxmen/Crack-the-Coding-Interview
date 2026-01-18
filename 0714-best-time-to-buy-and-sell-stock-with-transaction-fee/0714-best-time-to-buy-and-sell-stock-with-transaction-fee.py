class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        # 주식을 안 가질 때 / 가질때 최대 이익 값 저장하는 배열
        non = [0] * n
        take = [0] * n

        non[0] = 0
        take[0] = -prices[0] # 주식을 '샀기' 때문에, 최대 이익은 -로 시작한다.

        for i in range(1, n):
            # 판다 = (팔기전 최대이익 + 지금 금액 - 수수료)
            selling = take[i-1] + prices[i] - fee

            # 산다 = (안샀을때 최대이익 - 지금가격)
            buying = non[i-1] - prices[i]

            non[i] = max(selling, non[i-1]) # 팔때, 안살때
            take[i] = max(buying, take[i-1]) # 살때, 안팔때

        return max(non[n-1], take[n-1])
