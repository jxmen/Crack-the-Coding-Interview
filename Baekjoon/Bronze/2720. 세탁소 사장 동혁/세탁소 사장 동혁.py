
def solution(c):
    """
    쿼터, 다임, 니켈, 페니의 개수 구하기
    """
    quarter, dime, nickel, penny = 0, 0, 0, 0

    while c >= 25:
        quarter += 1
        c -= 25

    while c >= 10:
        dime += 1
        c -= 10
    
    while c >= 5:
        nickel += 1
        c -= 5
    
    while c >= 1:
        penny += 1
        c -= 1
    
    return quarter, dime, nickel, penny

t = int(input())
cents = [int(input()) for _ in range(t)]

for c in cents:
    result = solution(c)
    print(*result)