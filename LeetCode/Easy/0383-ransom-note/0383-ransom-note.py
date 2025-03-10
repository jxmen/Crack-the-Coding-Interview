class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for c in magazine:
            hashmap[c] = 1 + hashmap.get(c, 0)

        for c in ransomNote:
            if c not in hashmap or hashmap[c] <= 0:
                return False
            hashmap[c] -= 1
        
        return True
