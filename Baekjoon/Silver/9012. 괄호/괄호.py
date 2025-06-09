n = int(input())

def is_correct(s):
    stack = []
    for c in list(s):
        if c == '(':
            stack.append(c)
        else:
            if not len(stack):
                return False
            else:
                stack.pop()

    return len(stack) == 0

for _ in range(n):
    s = input()
    print("YES" if is_correct(s) else "NO")