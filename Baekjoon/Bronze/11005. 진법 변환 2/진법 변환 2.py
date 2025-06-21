def convert_to_char(c):
    if int(c) < 10:
        return str(c)
    else:
        return chr(int(c) + 55)         

# 10진법 n -> b진법 으로 변환
def solution(n, b):
    strs = []

    while n > 0:
        strs.append(n % b)
        n //= b

    return ''.join(
        list(
            reversed(
                [convert_to_char(c) for c in list(strs)])
            )
        )

if __name__ == "__main__":
    n, b = map(int, input().split())
    print(solution(n, b))
