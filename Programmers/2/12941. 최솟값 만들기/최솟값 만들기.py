"""
[1,4,2], [5,4,4]
한개의 숫자를 뽑는다
A에서 1번째 1, B에서 첫번째 => 0 + 1 * 5 = 5
A.. 2, B... 3 => 5 + 4 * 4 = 21

최소가 되는 경우의 숫자를 리턴하라.

===
최소인 것을 어떻게 확일할 것인가 ?
1. A에서 가장 작은 수 / B에서 가장 큰 수 끼리?
- 가장 큰 값들끼리 곱하면 값이 커질 것이다.
- [1,2,3] / [6,5,4] => 6 + 10 + 12 = 28

"""

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer