from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS로 해결하자.
# X부터 시작해서 최단거리가 K인 도시의 번호들을 모두 찾자.
distance = [-1] * (n + 1)
distance[x] = 0
queue = deque([x])
while queue:
    current = queue.popleft()
    for next_node in graph[current]:
        if distance[next_node] == -1:
            distance[next_node] = distance[current] + 1
            queue.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
