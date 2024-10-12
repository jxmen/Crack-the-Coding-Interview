class Solution:

    # TODO: change code to bottom-up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True

        for word in wordDict:
            if s.startswith(word):
                newStr = s[len(word):]
                if self.wordBreak(s=newStr, wordDict=wordDict) == True:
                    return True
            
        return False