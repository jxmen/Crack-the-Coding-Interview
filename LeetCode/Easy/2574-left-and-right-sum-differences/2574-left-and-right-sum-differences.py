class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sums = [0] * n
        right_sums = [0] * n

        right_sums[0] = sum(nums) - nums[0]
        left_sums[n-1] = sum(nums) - nums[n-1]
        for i in range(1, n):
            num = nums[i]
            right_sums[i] = right_sums[i-1] - num
        
        for i in range(n-2, -1, -1):
            num = nums[i]
            left_sums[i] = left_sums[i+1] - num
        
        answer = [0] * n
        for i in range(n):
            result = left_sums[i] - right_sums[i]
            answer[i] = result if result > 0 else (result * -1)
        
        return answer
