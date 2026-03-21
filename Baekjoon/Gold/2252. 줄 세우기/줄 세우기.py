import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    node = queue.pop()
    answer.append(node)

    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(' '.join(map(str, answer)))
