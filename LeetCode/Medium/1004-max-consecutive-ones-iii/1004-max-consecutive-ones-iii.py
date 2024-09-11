class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 현재 자리수가 0인 것을 최대 k만큼 1로 바꿔서 sliding window가 얼마나 유지되는지 확인한다.
        longest = 0
        zeros = 0
        i = 0 

        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            j += 1
            
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            
            longest = max(longest, (j-i))
        
        return longest
