class Solution:
    def missingNumber2(self, nums: List[int]) -> int:
        # TODO: Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
        pass

    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums) # space O(N), time O(N)
        for i in range(len(nums)+1): # time O(N)
            if i not in numSet:
                return i
        
        return -1
        