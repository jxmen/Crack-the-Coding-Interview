import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        start, end = 0, n - 1

        front_heap, back_heap = [], []

        # 초기 후보 채우기
        while start <= end and len(front_heap) < candidates:
            heapq.heappush(front_heap, (costs[start], start))
            start += 1

            if start <= end:
                heapq.heappush(back_heap, (costs[end], end))
                end -= 1

        for _ in range(k):
            # 한쪽 힙이 비어 있는 경우
            if not back_heap or (front_heap and front_heap[0] <= back_heap[0]):
                cost, _ = heapq.heappop(front_heap)
                ans += cost

                # front에서 뽑았으므로 front 쪽에서만 보충
                if start <= end:
                    heapq.heappush(front_heap, (costs[start], start))
                    start += 1
            else:
                cost, _ = heapq.heappop(back_heap)
                ans += cost

                # back에서 뽑았으므로 back 쪽에서만 보충
                if start <= end:
                    heapq.heappush(back_heap, (costs[end], end))
                    end -= 1

        return ans