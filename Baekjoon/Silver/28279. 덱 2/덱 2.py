import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command.startswith("1"):
        num = command.split(' ')[1]
        queue.appendleft(num)
    elif command.startswith("2"):
        num = command.split(' ')[1]
        queue.append(num)
    elif command == "3":
        print(queue.popleft() if queue else -1)
    elif command == "4":
        print(queue.pop() if queue else -1)
    elif command == "5":
        print(len(queue))
    elif command == "6":
        print(1 if not queue else 0)
    elif command == "7":
        print(queue[0] if queue else -1)
    elif command == "8":
        print(queue[-1] if queue else -1)
    else:
        raise Exception("지원되지 않는 명령어")

