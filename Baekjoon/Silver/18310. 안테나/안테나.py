def solution(n, numbers):
    # O(NlogN)
    sorted_numbers = sorted(numbers)

    # 중간에 해당하는 값이, 내 거리와 얼마나 차이나는지 확인하자.
    middle_index = (n - 1) // 2
    return sorted_numbers[middle_index]


n = int(input())
numbers = list(map(int, input().split(' ')))

print(solution(n, numbers))
