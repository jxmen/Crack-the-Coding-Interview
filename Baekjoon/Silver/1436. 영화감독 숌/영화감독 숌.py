def solution(n):
    """
    1: 666
    2: 1666
    5: 5666
    187: 66666
    500: 166699
    """
    count = 1
    number = 666
    
    # count가 n이 될때까지 반복하고, 숫자를 계속해서 늘린다. 666이 포함되어 있다면 count를 늘린다.
    while count != n:
        number += 1
        
        # number가 '666'이 포함되어있는지 체크한다. 있다면 count 증가
        if '666' in str(number):
            count += 1
    
    return number

n = int(input())

print(solution(n))