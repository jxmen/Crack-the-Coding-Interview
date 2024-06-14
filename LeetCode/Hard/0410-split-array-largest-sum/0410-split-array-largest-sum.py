class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start, end = max(nums), sum(nums)

        while start <= end:
            middle = (start+end) // 2
            if self.cntNumOfSplits(nums, middle) <= k:
                end = middle - 1
            else:
                start = middle + 1

        return start

    def cntNumOfSplits(self, nums, middle):
        cntNumOfSplits=1
        total=0

        for num in nums:
            if (total + num) <= middle:
                total += num
            else:
                cntNumOfSplits += 1
                total = num

        return cntNumOfSplits;
