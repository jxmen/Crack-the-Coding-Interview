class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []
        def backtrack(start, nums, current_sum):
            if sum(nums) == target:
                sums.append(nums[:])
                return
            elif sum(nums) > target:
                return

            for i in range(start, len(candidates)):
                nums.append(candidates[i])
                backtrack(i, nums, current_sum + candidates[i])
                nums.pop() 
        
        backtrack(start=0, nums=[], current_sum=0)
        return sums
