from collections import deque

n = int(input())
nums = list(map(int, input().split()))

queue = deque()
for i in range(n):
    num = nums[i]
    queue.append([num, i+1])

result = []
while queue:
    move, idx = queue.popleft()
    result.append(idx)

    if not queue:
        break

    queue.rotate(-(move - 1) if move > 0 else -move)

print(' '.join(map(str, result)))