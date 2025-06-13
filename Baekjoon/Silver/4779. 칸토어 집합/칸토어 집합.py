def solution(n):
    # 3^n만큼에 해당하는 문자열을 만든다.
    if n == 0:
        return '-'

    s = '-' * pow(3, n)

    # 문자열 가운데를 공백으로 바꾼다.
    # 1/3에 해당하는 문자열 길이를 찾는다. 그리고 문자열+공백+문자열 형태로 만든다.
    new_str_length = len(s) // 3
    new_str = solution(n-1)

    return new_str + (' ' * new_str_length) + new_str

import sys

for line in sys.stdin:
    n = int(line.strip())
    print(solution(n))
