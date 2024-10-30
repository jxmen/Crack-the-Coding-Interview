from collections import deque

def solution(cards1, cards2, goal):
    n, goal_pointer = len(goal), 0
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    
    while goal_pointer < n:
        if len(cards1_queue) and cards1_queue[0] == goal[goal_pointer]:
            cards1_queue.popleft()
            goal_pointer += 1
        elif len(cards2_queue) and cards2_queue[0] == goal[goal_pointer]:
            cards2_queue.popleft()
            goal_pointer += 1
        else:
            return "No"
    
    return "Yes"
