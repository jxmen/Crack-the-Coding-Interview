from typing import List
from unittest import TestCase

def find_target_row(matrix: List[List[int]], target: int) -> List[int]:
    if len(matrix) == 1:
        return matrix[0]

    target_row = None
    start = 0
    end = len(matrix)
    while start <= end:
        mid = (start + end) // 2
        if mid >= len(matrix):
            return None

        mid_row = matrix[mid]
        mid_row_start = mid_row[0]
        mid_row_end = mid_row[len(mid_row) - 1]

        if mid_row_start <= target <= mid_row_end:
            target_row = mid_row
            break

        if target > mid_row_end:
            start = mid + 1
        else:
            end = mid - 1

    return target_row


def is_target_in_row(target: int, target_row: List[int]) -> bool:
    if len(target_row) == 1:
        return target_row[0] == target

    start = 0
    end = len(target_row)
    while start <= end:
        mid = (start + end) // 2
        if mid >= len(target_row):
            return False

        mid_value = target_row[mid]
        if mid_value == target:
            return True

        if target < mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        m * n 매트릭스가 주어질 때 아래의 2개의 조건을 충족한다.
        - 각각의 열을 오름차순으로 정렬된다.
        - 열의 첫번째 정수는 전 열의 마지막 정수보다 크다.
        target이 주어질 때, target이 matrix에 있으면 true, 아닐 경우 false를 리턴하는 함수를 작성하시오.
        O(log(m * n)) 시간복잡도로 풀어야 합니다.
        """

        # target이 어떤 열에 속하는지 먼저 찾는다.
        target_row = find_target_row(matrix, target)
        if target_row is None:
            return False

        # target_row 안에서 target을 찾는다. 없으면 false를 리턴한다.
        # log(n) 만에 target을 찾아야 한다.
        return is_target_in_row(target, target_row)