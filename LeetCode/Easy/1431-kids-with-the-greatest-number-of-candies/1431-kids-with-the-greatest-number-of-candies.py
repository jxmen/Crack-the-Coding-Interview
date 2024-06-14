"""
사탕을 가지고 있는 아이들이 n명 있습니다. 각 candies[i]는 i번째 아이가 가지고 있는 사탕의 수를 나타내는 정수 배열 사탕이 주어지고, 여분의 사탕 수를 나타내는 정수 extraCandies가 주어집니다.

length n이 주어질 때 result[i]가 i번째 아이에게 추가 캔디를 주었을 때 가장 큰 값이면 result[i]에 true를 할당하고, 아닐 경우 false를 할당한다.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        
        return map(lambda x: (x + extraCandies) >= maxCandies, candies)
