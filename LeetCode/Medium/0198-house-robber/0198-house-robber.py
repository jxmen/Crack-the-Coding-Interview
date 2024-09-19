class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
  
        """
        맨 뒤에서부터 계산하자 (자기 자신의 값이 확정된 값이다!)
        [10, 2, 3, 100, 4]
        dp[n-1] = nums[n-1] = 4
        dp[n-2] = num[n-2] = 100
        dp[n-3] = nums[n-3] + max(dp[n-3+2:])
        dp[n-4] = nums[n-4] + max(dp[n-4+2:])
        """

        # dp[n-1], dp[n-2] 세팅
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]

        # dp 계산
        for i in range(n-3, -1, -1):
            dp[i] = nums[i] + max(dp[i+2:])
        
        return max(dp)