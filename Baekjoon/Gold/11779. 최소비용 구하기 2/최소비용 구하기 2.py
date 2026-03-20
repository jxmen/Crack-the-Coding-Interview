import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, n, start, target):
    d = [float('inf')] * (n + 1)
    d[start] = 0
    prev = [-1] * (n + 1)

    pq = [(0, start)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > d[node]:
            continue

        for next_node, edge_cost in graph[node]:
            new_cost = edge_cost + d[node]
            if new_cost < d[next_node]:
                d[next_node] = new_cost
                prev[next_node] = node
                heapq.heappush(pq, (new_cost, next_node))

    if prev[target] == -1 and target != start:
        return []

    path = [target]
    index = target
    while prev[index] != -1:
        path.append(prev[index])
        index = prev[index]

    path.reverse()
    return d[target], path


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, target = map(int, input().split())

min_cost, path = dijkstra(graph, n, start, target)
print(min_cost)
print(len(path))
print(' '.join(map(str, path)))
