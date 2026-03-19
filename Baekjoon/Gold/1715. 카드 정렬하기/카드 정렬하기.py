import heapq
import sys

input = sys.stdin.readline


def solution(numbers):
    heap = numbers
    heapq.heapify(heap)

    answer = 0
    while len(heap) > 1:
        n1, n2 = heapq.heappop(heap), heapq.heappop(heap)
        number_sum = n1 + n2

        heapq.heappush(heap, number_sum)
        answer += number_sum

    return answer


n = int(input())
numbers = [int(input()) for _ in range(n)]

print(solution(numbers))
