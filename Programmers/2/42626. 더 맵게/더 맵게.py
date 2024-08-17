import heapq

def solution(scoville, K):
    answer = 0
    minHeap = []
    for s in scoville:
        heapq.heappush(minHeap, s)
        
    while len(minHeap) > 1:
        # 2개를 꺼내고 다시 힙에 넣는다.
        first = heapq.heappop(minHeap)
        
        # 모든 값이 K 이상이여야 하므로, 최소값인 K를 넘으면 바로 리턴한다.
        if first >= K:
            return answer

        second = heapq.heappop(minHeap)
        shaked = first + (second * 2)
        heapq.heappush(minHeap, shaked)
        answer += 1
    
    if minHeap[0] >= K:
        return answer
        
    return -1
