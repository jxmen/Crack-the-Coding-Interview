import sys

n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

nums.sort()
for num in nums:
    print(num)
