from collections import deque

def solution(priorities, location):
    answer = 1 # 몇번째로 실행되는지를 나타내는 값
    
    queue = deque(priorities)
    while queue:
        popped = queue.popleft()
        if not queue:
            return answer
        
        # 큐에서 꺼내야 하는(우선순위가 가장 높은) 값이라면, location과 answer도 업데이트 해준다.
        if popped >= max(queue):
            # location 값 업데이트
            if location == 0:
                return answer
            else:
                location -= 1
            
            answer += 1 
        else:
            # 우선순위가 더 높은 값이 큐에 있다면 다시 맨 뒤로 집어넣는다.
            queue.append(popped)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
    
    return -1