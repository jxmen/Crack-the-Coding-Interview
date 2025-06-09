import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command.startswith('push'):
        num = int(command.split(' ')[1])
        queue.append(num)
    elif command == 'pop':
        print(queue.popleft() if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(1 if not queue else 0)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)



