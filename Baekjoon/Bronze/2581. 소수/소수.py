import math

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def get_primes(start, end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)

    return primes
    

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    
    primes = get_primes(m, n)
    if not len(primes):
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))
