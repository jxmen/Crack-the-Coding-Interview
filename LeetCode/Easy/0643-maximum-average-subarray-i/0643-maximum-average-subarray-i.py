class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 1. 처음에는 [:k]까지 먼저 찾는다.
        subArr = nums[:k]
        subArrSum = sum(subArr)
        maxAvg = subArrSum / k

        # 2. 그 다음에는 array의 맨 끝까지 찾는다.
        for i in range(k, len(nums)):
            subArrSum += nums[i]
            subArrSum -= nums[i-k]
            maxAvg = max(subArrSum / k, maxAvg)
        
        return maxAvg
