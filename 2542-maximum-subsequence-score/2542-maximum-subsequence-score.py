import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        n = len(nums1)

        tuples = []
        for i in range(n):
            tuples.append((nums2[i], nums1[i]))
        tuples.sort(reverse=True)

        nums1_sum = 0
        heap = []
        for t in tuples:
            num2, num1 = t
            heapq.heappush(heap, num1)
            nums1_sum += num1

            # k개 초과 시 가장 작은 nums1 제거
            if len(heap) > k:
                nums1_sum -= heapq.heappop(heap)

            # 정확히 k개일 때 점수 계산
            if len(heap) == k:
                ans = max(ans, nums1_sum * num2)

        return ans
