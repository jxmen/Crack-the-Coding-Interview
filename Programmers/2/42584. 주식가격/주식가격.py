def solution(prices):
    answer = [0] * len(prices) # 떨어지지 않는 주식 가격들을 담을 목록
    stack = []
    for i in range(len(prices)):
        # [2,3,1]과 같이 전에 꺼낸 값이 계속 떨어지지 않았는지 체크하는 로직이 필요하다.
        while stack and prices[stack[-1]] > prices[i]:
            p = stack.pop()
            answer[p] = i - p
        stack.append(i)
    
    # 스택이 남아있다면, 해당 인덱스들은 prices가 끝날때까지 주식 가격이 떨어지지 않은 것이다. 남은 처리를 진행한다.
    while stack:
        popped = stack.pop()
        # prices가 끝날때까지 주식 가격이 떨어지지 않은 것이므로, len(prices) - 1 만큼 빼준다
        answer[popped] = (len(prices) - 1) - popped
    
    return answer
