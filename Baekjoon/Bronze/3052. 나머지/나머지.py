nums = [int(input()) for _ in range(10)]
num_set = set()
for num in nums:
    num_set.add(num % 42)

print(len(num_set))