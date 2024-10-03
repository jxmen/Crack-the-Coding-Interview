s = str(input())
bomb = str(input())

stack = []
for c in s:
    stack.append(c)
    if len(stack) >= len(bomb) and stack[-len(bomb):] == list(bomb):
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
