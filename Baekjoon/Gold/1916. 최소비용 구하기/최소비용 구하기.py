import heapq
import sys

input = sys.stdin.readline


def solution(graph, start, end):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cur_cost, city = heapq.heappop(heap)
        if cur_cost > dist[city]: # 이미 처리된 도시 건너뛰기
            continue

        for next, edge_cost in graph[city]:
            new_cost = dist[city] + edge_cost
            if new_cost < dist[next]: # 더 저렴한 경로 발견 시에만
                dist[next] = new_cost # 최단거리 업데이트
                heapq.heappush(heap, (new_cost, next))

    return dist[end]


city_count = int(input())
bus_count = int(input())
graph = [[] for _ in range(city_count + 1)]

for _ in range(bus_count):
    start_city_number, end_city_number, cost = map(int, input().split())
    graph[start_city_number].append((end_city_number, cost))

start, end = map(int, input().split())
print(solution(graph, start, end))
