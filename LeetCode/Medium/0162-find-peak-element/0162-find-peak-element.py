class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        return self.findPeakElementHelp(nums, start=0, end=n-1)
    
    def findPeakElementHelp(self, nums: List[int], start: int, end: int) -> int:
        if len(nums) == 1:
            return 0

        if end - start == 1:
            return start if nums[start] > nums[end] else end
        
        mid = (start + end) // 2
        leftNums = nums[start:mid]
        rightNums = nums[mid:end]
        maxLeftNum = max(leftNums)
        maxRightNum = max(rightNums)
        if max(leftNums) == max(rightNums):
            return leftNums.index(max(leftNums))

        if maxLeftNum > maxRightNum:
            return self.findPeakElementHelp(nums, start=start, end=mid)
        else:
            return self.findPeakElementHelp(nums, start=mid, end=end)
        