import sys
input = sys.stdin.readline

n = int(input())

counts = [0] * 10001

for _ in range(n):
    num = int(input())
    counts[num] += 1

for i in range(1, 10001):
    for j in range(counts[i]):
        print(i)
