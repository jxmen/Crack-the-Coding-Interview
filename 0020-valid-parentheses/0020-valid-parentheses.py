class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue

            if not len(stack):
                return False

            stack_last = stack.pop()
            if pairs[stack_last] != c:
                return False

        return len(stack) == 0
