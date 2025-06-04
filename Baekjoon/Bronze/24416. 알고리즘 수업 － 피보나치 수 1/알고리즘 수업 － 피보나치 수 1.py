n = int(input())

def fib_recursive(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1

    cache[n] = fib_recursive(n-1, cache) + fib_recursive(n-2, cache)
    return cache[n]

def fib_dp(n, count=0):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        count += 1

    return count

fib_recursive_count, fib_dp_count = fib_recursive(n), fib_dp(n)
print(fib_recursive_count, fib_dp_count)
