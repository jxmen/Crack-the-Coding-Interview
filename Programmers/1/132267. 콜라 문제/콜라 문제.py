"""
a: 줘야 하는 병 수
b: a개를 주면 주는 병 수
n: 현재 가진 병 수

1. answer에 b * (n / a)를 추가한다 (answer += (b * (n / a)))
2. n을 n에서 a로 나눈 값으로 할당한다 (n: 20, a:2일 경우 n = n/a = 20/2 = 10)

20 / 3 = 6.xxxx

n = (20 // 3) + 2
2 = 20 - (20 // 3 * 3)
"""

def solution(a, b, n):
    answer = 0
    while n >= a:
        # 마트에서 받은 병 추가
        new = b * (n // a)
        answer += new
        
        # 교환한 병 + 기존 병으로 변경
        n = (n % a) + new
        
    return answer
