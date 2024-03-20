class Solution:
    opens = set(list(['(', '[', '{']))
    d = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if self.is_open(c):
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False
            
            popped = stack.pop()
            if not self.validate(popped, c):
                return False
        
        return len(stack) == 0

    def is_open(self, c: str) -> bool:
        return c in Solution.opens

    def validate(self, popped: str, c: str) -> bool:
        return Solution.d[popped] == c

        