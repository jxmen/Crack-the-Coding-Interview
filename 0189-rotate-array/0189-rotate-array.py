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
        
        newNums = [] # TODO: space O(1) 만에 해결할 수 있는 방법을 찾아야 한다.
        while len(queue) > 0:
            newNums.append(queue.popleft())
        
        for i in range(len(nums)):
            nums[i] = newNums[i]
    