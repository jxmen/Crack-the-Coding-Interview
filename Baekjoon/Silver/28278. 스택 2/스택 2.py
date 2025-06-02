import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().rstrip()

    if command.startswith('1'):
        _, value = command.split()
        stack.append(int(value))
    elif command == '2':
        print(stack.pop() if stack else -1)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(1 if not stack else 0)
    elif command == '5':
        print(stack[-1] if stack else -1)
