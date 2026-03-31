import sys
import heapq

input = sys.stdin.readline


def solution(n, arr):
    """
    힙을 2개 만든다. arr를 기반으로 최소 힙을 하나 만들어 모든 값을 넣고, 다른 하나의 힙은 기존 힙에서 값을 꺼내면서 넣는다.

    example:

    for _ in range(n):
        popped = heap1.pop()
        while popped[0] >= end[1]:
            heap2.pop()

        heap2.add(popped)
        ans = min(ans, len(heap2))
    """

    heap1, heap2 = arr[:], []
    heapq.heapify(heap1)

    ans = 0
    for _ in range(n):
        popped = heapq.heappop(heap1)
        while len(heap2) and popped[0] >= heap2[0][0]:
            heapq.heappop(heap2)

        heapq.heappush(heap2, (popped[1], popped[0]))
        ans = max(ans, len(heap2))

    return ans


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

print(solution(n, arr))
