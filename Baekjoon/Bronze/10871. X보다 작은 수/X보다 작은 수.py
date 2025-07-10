n, x = map(int, input().split())
nums = list(map(int, input().split()))

result = [str(num) for num in nums if num < x]
print(' '.join(result))