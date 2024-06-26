"""
0 1 0 3 12 (left = 0, right = 1)
swap -> 1 0 0 3 12

1 0 0 3 12 (left = 1, right = 2)
1 0 0 3 12 (left = 1, right = 3)
swap -> 1 3 0 0 12

1 3 0 0 12 (left = 2, right = 4)
swap -> 1 3 12 0 0
===


"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return

        # left, right two pointer 사용 시 right가 0인 것으로 체크하기 위해 미리 바꿔준다.
        if nums[0] == 0:
            p = 1
            while p < len(nums) and nums[p] == 0:
                p += 1
            
            if p < len(nums):
                nums[0], nums[p] = nums[p], nums[0]
        
        # right가 0이 있는 인덱스를 찾아서 left 인덱스에 있는 값과 교체한다.
        left, right = 1, 2
        while right < len(nums):
            # left는 0이 아닌 값일때까지, right는 0인 값을 찾는다.
            while left < right and nums[left] != 0:
                left += 1
            
            while right < len(nums) and nums[right] == 0:
                right += 1
            
            if left >= len(nums) or right >= len(nums):
                break
            
            # swap
            nums[left], nums[right] = nums[right], nums[left]
            
            left += 1
            right += 1
