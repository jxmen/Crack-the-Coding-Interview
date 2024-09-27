def solution(s):
    stack = []
    for c in list(s):
        if c == "(":
            stack.append(c)
            continue
        
        if len(stack) == 0:
            return False
        else:
            stack.pop()
           
    return len(stack) == 0
