def solution(ints, plus, minus, multiply, divide):
    n = len(ints)
    max_result = -float('inf')
    min_result = float('inf')

    def dfs(idx, current, p, m, mul, div):
        nonlocal max_result, min_result
        if idx == n:
            max_result = max(max_result, current)
            min_result = min(min_result, current)
            return
        if p:
            dfs(idx + 1, current + ints[idx], p - 1, m, mul, div)
        if m:
            dfs(idx + 1, current - ints[idx], p, m - 1, mul, div)
        if mul:
            dfs(idx + 1, current * ints[idx], p, m, mul - 1, div)
        if div:
            if current < 0:
                dfs(idx + 1, -(-current // ints[idx]), p, m, mul, div - 1)
            else:
                dfs(idx + 1, current // ints[idx], p, m, mul, div - 1)

    dfs(1, ints[0], plus, minus, multiply, divide)
    return [max_result, min_result]

if __name__ == '__main__':
    n = int(input())
    ints = list(map(int, input().split()))
    plus, minus, multiply, divide = map(int, input().split())

    result = solution(ints, plus, minus, multiply, divide)
    print(result[0])
    print(result[1])
