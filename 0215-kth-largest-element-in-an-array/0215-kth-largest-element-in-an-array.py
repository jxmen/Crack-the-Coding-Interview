import heapq

class Solution:
    # k 길이 만큼 최소힙을 쓰는 것이 더 적절하다.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap) # O(k)

        # k개 만큼 들어있으므로, k 인덱스 이후부터 순회한다.
        for num in nums[k:]:
            # 현재 값이 더 크면 교체
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]

    def findKthLargestWithMaxHeap(self, nums: List[int], k: int) -> int:
        # 최대힙 만들고 k-1번 pop 한 후 맨 앞의 값을 리턴한다.
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k-1):
            heapq.heappop(max_heap)
        
        return heapq.heappop(max_heap) * -1
