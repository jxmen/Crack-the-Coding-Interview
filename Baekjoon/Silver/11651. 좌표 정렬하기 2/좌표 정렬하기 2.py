n = int(input())

nums = []
for i in range(n):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort(key=lambda x: (x[1], x[0]))

for num in nums:
    print(num[0], num[1])
