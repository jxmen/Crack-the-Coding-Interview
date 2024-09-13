class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        zeros = 0
        longest = 0

        while p2 < len(nums):
            if nums[p2] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[p1] == 0:
                    zeros -= 1
                p1 += 1
            
            longest = max(longest, (p2-p1))
            p2 += 1

        return longest
        