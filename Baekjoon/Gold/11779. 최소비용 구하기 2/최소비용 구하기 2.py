import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start, end):
    n = len(graph)

    d = [float('inf')] * (n + 1)
    d[start] = 0
    prev = [0] * (n + 1)

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

    channel = [end]
    prev_index = end
    while prev[prev_index] != 0:
        channel.append(prev[prev_index])
        prev_index = prev[prev_index]

    channel.reverse()
    return [d[end], channel]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

min_cost, channel = dijkstra(graph, start, end)
print(min_cost)
print(len(channel))
print(' '.join(map(str, channel)))
