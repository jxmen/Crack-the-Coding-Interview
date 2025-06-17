import heapq

def solution(heard_people, saw_people):
    both_people = []
    heard_set = set(heard_people)
    for person in saw_people:
        if person in heard_set:
            heapq.heappush(both_people, person)
    
    result = []
    while both_people:
        result.append(heapq.heappop(both_people))
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())

    heard_people = []
    for _ in range(n):
        heard_people.append(input())

    saw_people = []
    for _ in range(m):
        saw_people.append(input())

    both_people = solution(heard_people, saw_people)
    print(len(both_people))
    for person in both_people:
        print(person)
