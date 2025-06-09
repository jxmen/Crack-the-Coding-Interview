def is_balance(s):
    stack = []
    for c in list(s):
        if c == '(' or c == '[':
            stack.append(c)
            continue

        if c == ')':
            if not len(stack) or stack[-1] != '(':
                return False

            stack.pop()

        if c == ']':
            if not len(stack) or stack[-1] != '[':
                return False

            stack.pop()


    return len(stack) == 0

while True:
    s = input()
    if s == ".":
        break

    print("yes" if is_balance(s) else "no")