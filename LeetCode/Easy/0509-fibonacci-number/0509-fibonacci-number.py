class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return n

        nums = [0] * (n+1)
        nums[0] = 0
        nums[1] = 1

        for i in range(2, n+1):
            nums[i] = nums[i-1] + nums[i-2]
        
        return nums[n]
