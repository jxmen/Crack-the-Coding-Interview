import sys
import heapq

input = sys.stdin.readline

N = int(input())
min_heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        # 정수 꺼내기
        if len(min_heap) > 0:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)



