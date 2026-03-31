import sys
import heapq

input = sys.stdin.readline


def solution(n, arr):
    ans = 0

    heap = [(end, start) for start, end in arr]
    heapq.heapify(heap)

    while heap:
        end, start = heapq.heappop(heap)
        while heap and end > heap[0][1]:
            heapq.heappop(heap)

        ans += 1

    return ans


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

print(solution(n, arr))
