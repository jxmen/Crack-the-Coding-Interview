class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # two pointer + hashmap

        # 처음 세팅
        hashmap = {} # 'a': 1, 'b': 2
        first, second = 0, 0
        maxLength = 0
        while second < len(s):
            if s[second] not in hashmap:
                hashmap[s[second]] = 1
            else:
                hashmap[s[second]] += 1
            
            while hashmap[s[second]] > 2:
                hashmap[s[first]] -= 1
                if hashmap[s[first]] == 0:
                    del hashmap[s[first]]
                
                first += 1
            
            maxLength = max(maxLength, second - first + 1)
            second += 1
                
        return maxLength
