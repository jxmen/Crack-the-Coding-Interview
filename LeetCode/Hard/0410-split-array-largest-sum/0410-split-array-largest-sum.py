class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start, end = max(nums), sum(nums)

        while start <= end:
            middle = (start+end) // 2
            if self.getSplitCount(nums, middle) <= k:
                end = middle - 1
            else:
                start = middle + 1

        return start
    
    """
    middle을 넘기지 않는 최대 분할 개수를 리턴한다.
    """
    def getSplitCount(self, nums: List[int], middle: int) -> int:
        splits = 1
        total = 0

        for num in nums:
            if (total + num) <= middle:
                total += num
            else:
                splits += 1
                total = num

        return splits
