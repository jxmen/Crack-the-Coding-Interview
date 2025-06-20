n, b = input().split()
b = int(b)

# b진법 n을 10진법으로 변환
def solution(n, b):
    result = 0
    for i in range(len(n)):
        idx = len(n) - i - 1
        
        # 현재 자릿수에 b의 i제곱을 곱함
        c = n[idx]
        result += pow(b, i) * (int(c) if c.isdigit() else ord(c) - 55)

    return result

print(solution(n, b))
