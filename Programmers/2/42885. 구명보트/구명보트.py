"""
[40,30,20,10], limit = 50
"""

def solution(people, limit):
    answer = 0
    people.sort()
    
    # 보트는 최대 2명. 투포인터 선언
    first, last = 0, len(people) - 1
    while first <= last:
        if people[first] + people[last] <= limit:
            # 가장 작은 사람도 태울 수 있다면 같이 태운다.
            first += 1
        
        last -= 1
        answer += 1
            
        
    return answer
    