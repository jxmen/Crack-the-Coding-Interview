def solution(n):
    nums = [i for i in range(1, n+1)]
    return sum(nums)

if __name__ == "__main__":
    n = int(input())
    print(solution(n))