import sys
sys.setrecursionlimit(10**9)

x = int(input())

cache = {1: 0}

def solution(n):
    if n in cache:
        return cache[n]

    min_count = solution(n - 1) + 1

    if n % 2 == 0:
        min_count = min(min_count, solution(n // 2) + 1)

    if n % 3 == 0:
        min_count = min(min_count, solution(n // 3) + 1)

    cache[n] = min_count
    return cache[n]

print(solution(x))
