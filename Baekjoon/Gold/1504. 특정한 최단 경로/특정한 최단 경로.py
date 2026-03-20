import heapq
import sys

input = sys.stdin.readline


def dijkstra(graph, start, end):
    dist = [float('inf')] * (len(graph) + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue

        for weight, next_node in graph[node]:
            new_cost = weight + dist[node]
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist[end]


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def calc_path(*args):
    costs = [dijkstra(graph, s, e) for s, e in args]
    return -1 if float('inf') in costs else sum(costs)

result1 = calc_path((1, v1), (v1, v2), (v2, n))
result2 = calc_path((1, v2), (v2, v1), (v1, n))

print(-1 if all(x == -1 for x in [result1, result2]) else min(r for r in [result1, result2] if r != -1))
