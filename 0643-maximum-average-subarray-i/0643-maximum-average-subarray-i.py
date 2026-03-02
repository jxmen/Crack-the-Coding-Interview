class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sub_arr_sum = sum(nums[0:k])
        max_avg = sub_arr_sum / k

        for i in range(1, n - k + 1):
            sub_arr_sum -= nums[i - 1]
            sub_arr_sum += nums[i + k - 1]

            max_avg = max(max_avg, sub_arr_sum / k)

        return max_avg
