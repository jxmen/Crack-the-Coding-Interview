class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        # 0과 1일 때의 최소로 갈 수 있는 숫자를 dp에 저장해놓자.
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            # dp[i]는 꼭대기로 가기 위한 최소의 값
            # [10, 15, 20] 일 경우 dp는 [25, 15, 30]
            # dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
                # 단, 이 경우에는 dp[i-1]과 dp[i-2]가 미리 계산되어야 함.
            
            # i번째에서 최소로 구할 수 있는 값을 찾고 dp에 저장
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        return min(dp[-1], dp[-2])
