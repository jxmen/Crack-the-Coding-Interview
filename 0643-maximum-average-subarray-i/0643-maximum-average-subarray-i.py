class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_arr_sum = sum(nums[0:k])
        max_sum = sub_arr_sum

        for i in range(1, len(nums) - k + 1):
            sub_arr_sum += nums[i + k - 1] - nums[i - 1]
            max_sum = max(max_sum, sub_arr_sum)

        return max_sum / k
