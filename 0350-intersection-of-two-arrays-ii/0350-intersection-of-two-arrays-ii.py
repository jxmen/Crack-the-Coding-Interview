"""
[1,2,2,1], [2,2] -> [2,2]
[4,9,5], [9,4,9,8,4] -> [9,4]

1. two pointer? (안됨. p1에서 이미 지나간 요소에서 교차하는 숫자가 있을 수 있음)
2. N*M 배열 돌리기 (시간 복잡도 O(N*M))
3. n1을 카운터로 만들고, n2를 순회하면서 숫자를 감소시키고 리스트에 해당 숫자를 추가한다.  

"""

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        ans = []

        for num in nums2:
            if counter[num] > 0:
                ans.append(num)
                counter[num] -= 1

        return ans
