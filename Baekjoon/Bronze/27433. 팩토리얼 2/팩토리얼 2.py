def solution(n):
    if n == 0:
        return 1
    
    # n! = (n-1)! * n
    return solution(n-1) * n

n = int(input())
print(solution(n))