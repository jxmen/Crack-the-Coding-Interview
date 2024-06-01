class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set()
        for i in range(len(nums)):
            if (target - nums[i]) in numbers:
                j = nums.index(target - nums[i]) # 이부분도 잘못하면 O(N)이 걸릴 수도 있다.
                return [i, j]
            else:
                numbers.add(nums[i])
        