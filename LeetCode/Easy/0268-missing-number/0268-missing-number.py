class Solution:
    
    # only O(1) extra space complexity and O(n) runtime complexity?
    def missingNumber(self, nums: List[int]) -> int:
        # 공간을 어떻게 1개만 쓰고 풀 수 있을까? - 합계 공식을 사용하자.

        # n = 10이라면 sum = 45가 되어야 한다.
        # 만약 8이 빠졌다면 45-8 = 37일 것이다. (n은 하나가 빠졌으므로 +1 해준다.)
        nNumsSum = sum([i for i in range(len(nums)+1)])
        return nNumsSum - sum(nums)

    # set을 이용한 풀이 - space O(N), time O(N)
    def missingNumber2(self, nums: List[int]) -> int:
        numSet = set(nums) # space O(N), time O(N)
        for i in range(len(nums)+1): # time O(N)
            if i not in numSet:
                return i
        
        return -1
        