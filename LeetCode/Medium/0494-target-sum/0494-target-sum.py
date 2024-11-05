class Solution:

    # 메모이제이션을 사용한 코드
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(total, index):
            if index == len(nums):
                return 1 if total == target else 0
            
            if (index, total) in memo:
                return memo[(index, total)]
            
            add = backtrack(total = total + nums[index], index = index + 1)
            subtract = backtrack(total = total - nums[index], index = index + 1)

            memo[(index, total)] = add + subtract
            return memo[(index, total)]

        return backtrack(total = 0, index = 0)

    # NOTE: 메모이제이션 코드를 쓰지 않으면 비효율적이다.
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        def backtrack(total, index):
            if index == len(nums):
                return 1 if total == target else 0
            
            add = backtrack(total = total + nums[index], index = index + 1)
            subtract = backtrack(total = total - nums[index], index = index + 1)

            return add + subtract

        return backtrack(total = 0, index = 0)
