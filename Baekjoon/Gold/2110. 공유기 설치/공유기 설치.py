def can_place_routers(distance, c, houses):
    # greedy로 접근하여, 첫집과 거리가 distnace 만큼 차이나는 집에 바로 설치한다.
    count = 1
    last_pos = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_pos >= distance:
            count += 1
            last_pos = houses[i]

        if count >= c:
            return True

    return False

def solution(c, houses):
    houses.sort()

    low, high = 1, max(houses) - min(houses)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place_routers(mid, c, houses):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

if __name__ == '__main__':
    n, c = map(int, input().split())
    houses = []
    for _ in range(n):
        houses.append(int(input()))
    print(solution(c, houses))
