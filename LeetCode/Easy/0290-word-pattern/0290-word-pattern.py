class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordSet = set()
        dict = {}

        strs = s.split(" ")
        patterns = list(pattern)
        if len(strs) != len(patterns):
            return False
        
        for i in range(len(patterns)):
            p = patterns[i]
            if strs[i] in wordSet and not p in dict:
                return False

            if len(dict) == 0 or not p in dict:
                dict[p] = strs[i]
                wordSet.add(strs[i])
                continue
            
            if dict[p] != strs[i]:
                return False
        
        return True
