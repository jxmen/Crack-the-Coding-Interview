class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        max_nested_levels = 0
        
        for c in list(s):
            if c == '(':
                stack.append(c)
                continue
            
            if c == ')':
                if len(stack) > max_nested_levels:
                    max_nested_levels = len(stack)
                stack.pop()
                
        return max_nested_levels
        