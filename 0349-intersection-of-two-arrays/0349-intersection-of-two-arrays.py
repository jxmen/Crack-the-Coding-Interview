"""
[1,2,2,1], [2,2] -> [2]
[4,9,5], [9,4,9,8,4] -> [9,4]

sum 교집합 연산자를 사용하자.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
