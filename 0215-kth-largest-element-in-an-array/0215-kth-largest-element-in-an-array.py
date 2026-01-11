import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 최대힙 만들고 k-1번 pop 한 후 맨 앞의 값을 리턴한다.
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k-1):
            heapq.heappop(max_heap)
        
        return heapq.heappop(max_heap) * -1
