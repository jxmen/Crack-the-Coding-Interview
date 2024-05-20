class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque(nums)

        # rotate
        for i in range(0, k):
            popped = queue.pop()
            queue.appendleft(popped)
        
        newNums = [] # space O(N)
        while len(queue) > 0:
            newNums.append(queue.popleft())
        
        for i in range(len(nums)):
            nums[i] = newNums[i]
    