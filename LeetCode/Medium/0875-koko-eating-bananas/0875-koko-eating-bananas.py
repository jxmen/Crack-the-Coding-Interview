import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k, piles, h):
            hours_needed = 0
            for pile in piles:

                # k = 4, pile = 30일 때 30 / 4 = ceil(7.5) = 8 추가
                hours_needed += math.ceil(pile / k)
                if hours_needed > h:
                    return False
            return True

        # 1, max에서 binary search 진행
        start, end = 1, max(piles)
        answer = end
        while start <= end:
            mid = (start + end) // 2
            if can_eat(mid, piles, h):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1

        return answer
