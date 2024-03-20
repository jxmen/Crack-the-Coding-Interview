class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = set(list(['(', '[', '{']))
        for c in list(s):
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if not self.validate(popped, c):
                    return False
        
        return len(stack) == 0

    def validate(self, popped: str, c: str) -> bool:
        # chante to dict

        if popped == '(' and c != ')':
            return False
        if popped == '[' and c != ']':
            return False
        if popped == '{' and c != '}':
            return False
        
        return True

        