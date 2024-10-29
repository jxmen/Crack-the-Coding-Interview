from heapq import heappush, heappop

def solution(k, score):
    answer = []
    scores = []
    for s in score:
        if len(scores) < k:
            heappush(scores, s)
            answer.append(scores[0])
            continue
        
        if s < scores[0]:
            answer.append(scores[0])
        else:
            heappop(scores)
            heappush(scores, s)
            answer.append(scores[0])
    
    return answer
