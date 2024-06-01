class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited = s.split(" ")
        
        a_list = list(
            filter(
                lambda x: x != '', map(lambda x: x.strip(), splited)
            )
        )
        
        return len(a_list.pop())
            
