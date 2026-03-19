import heapq
import sys

input = sys.stdin.readline


def solution(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if cost > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist


n, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

result = solution(graph, start, n)
for i in range(1, n + 1):
    print(result[i] if result[i] != float('inf') else 'INF')
