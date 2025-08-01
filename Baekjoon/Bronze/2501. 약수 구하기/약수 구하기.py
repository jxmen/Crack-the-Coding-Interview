def kth_divisor(n, k):
    divisor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
            if divisor_count == k:
                return i
    return 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(kth_divisor(n, k))