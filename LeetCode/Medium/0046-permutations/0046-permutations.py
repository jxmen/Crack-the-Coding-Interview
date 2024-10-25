class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        result = []
        backtrack([])
        return result