class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = [0] * len(nums)
        total = [0] * len(nums)

        current[0], total[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            # 현재 값 중에 가장 큰 값은, 자기 자신을 포함하거나 포함하지 않고 자기 자신만
            current[i] = max(nums[i], current[i-1] + nums[i])

            total[i] = max(total[i-1], current[i])
        
        return total[len(nums) - 1]
