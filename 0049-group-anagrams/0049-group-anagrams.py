"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

"""
아나그램이면 서로 같은 키를 쓰도록 해야 함
["abc", "bca"] -> abc_key 

1. 각 문자마다 아스키 코드를 쓰고, sum으로 아나그램을 판별한다?
- 안됨XX "ad", "bc"의 경우 같은 아나그램으로 인식하게 됨.
2. 아스키 코드의 곱셈 값을 키로 쓰기?
3. 문자열 정렬한 값을 키로 쓰기

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            key = ''.join(sorted(s))
            group[key] = group.get(key, []) + [s]

        return list(group.values())
