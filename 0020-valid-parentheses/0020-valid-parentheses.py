class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack or pairs[stack.pop()] != c:
                return False
        return not stack
