n, x = map(int, input().split())
numbers = [int(x) for x in input().split()]


# 이진탐색으로 숫자 x를 찾고, (x의 마지막 인덱스 - x의 첫번째 인덱스 + 1의 값을 출력하자.)
def find_last_idx(numbers, x):
    start, end = 0, len(numbers) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == x:
            result = mid
            start = mid + 1
        elif numbers[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return result


def find_first_idx(numbers, x):
    start, end = 0, len(numbers) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == x:
            result = mid
            end = mid - 1
        elif numbers[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return result


def solution(n, x, numbers):
    """
    numbers에서 x가 등장하는 횟수를 리턴한다.

    :param n: numbers의 길이
    :param x: 찾을 숫자
    :param numbers: 숫자 목록 리스트
    :return: numbers에서 x가 등장하는 횟수
    """

    # x의 위치를 먼저 찾는다.
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == x:
            return find_last_idx(numbers, x) - find_first_idx(numbers, x) + 1

        if numbers[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return 0


print(solution(n, x, numbers))
