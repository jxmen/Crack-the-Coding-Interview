def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split(' ')))
    
    print(sum(is_prime(num) for num in nums))
