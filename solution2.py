def solution(n):
    answer = 0
    memo = {}

    def backtrack(start, total, numbers, multiply):
        nonlocal answer
        if total == n:
            if len(numbers) >= 2:
                answer = max(answer, multiply)
            return

        if total in memo and memo[total] >= multiply:
            return

        memo[total] = multiply

        for i in range(start, n+1):
            if total + i <= n:
                numbers.append(i)
                multiply *= i
                backtrack(i, total+i, numbers, multiply)
                multiply //= numbers.pop()

    backtrack(start=1, total=0, numbers=[], multiply=1)
    return answer


print(solution(2)) # 1
print(solution(3)) # 2
print(solution(5)) # 6
print(solution(8)) # 18
print(solution(100)) #

