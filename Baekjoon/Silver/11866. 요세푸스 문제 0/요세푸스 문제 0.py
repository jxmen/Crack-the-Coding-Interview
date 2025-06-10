from collections import deque

n, k = map(int, input().split())
result = []
queue = deque([i for i in range(1, n+1)])

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())

    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
