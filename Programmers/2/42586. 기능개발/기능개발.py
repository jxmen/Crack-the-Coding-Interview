from collections import deque

def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    pq = deque(progresses) # progresses queue
    sq = deque(speeds) # speeds queue
    while pq:
        for i in range(len(pq)):
            pq[i] += sq[i]
        
        if pq[0] >= 100:
            count = 0
            while pq and pq[0] >= 100:
                count += 1
                pq.popleft()
                sq.popleft()
            
            answer.append(count)
    
    return answer