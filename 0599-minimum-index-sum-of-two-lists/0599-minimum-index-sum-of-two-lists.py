"""
[h, s, g], [s, h, g]
h = 0 + 1 = 1
s = 1 + 0 = 1
g = 2 + 2 = 4

=> h, s

map1: h:0, s:1, g:2

for i, el in enumberate(list2):
    if el in map1:
        ans.append((el, map1.get(el) + i))
        
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        ans = []
        map1 = {}
        for i, el in enumerate(list1):
            map1[el] = i
        
        min_index_sum = float('inf')
        for i, el in enumerate(list2):
            if el in map1:
                index_sum = map1.get(el) + i
                
                ans.append((el, index_sum))
                min_index_sum = min(min_index_sum, index_sum)
        
        return list(
            map(lambda x: x[0], 
                filter(lambda x: x[1] == min_index_sum, ans)
            )
        )
