class Solution:
    def canJump(self, nums: List[int]) -> bool:
        indexes = set()

        return self.canJumpHelp(nums, 0, indexes)

    def canJumpHelp(self, nums: List[int], start: int, indexes: Set[int]) -> bool:
        if start >= len(nums): 
            return False
        elif start == len(nums) - 1:
            return True

        jump_count = nums[start]
        for i in range(jump_count, 0, -1):
            if len(nums) - i <= 0:
                continue
            
            if start + i in indexes:
                continue
            
            if self.canJumpHelp(nums, start + i, indexes):
                return True
            
            indexes.add(start + i)
        
        return False
