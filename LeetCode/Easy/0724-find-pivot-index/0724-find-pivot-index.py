"""
피벗 인덱스는 인덱스 왼쪽에 있는 모든 숫자의 합이 인덱스 오른쪽에 있는 모든 숫자의 합과 동일한 인덱스입니다.

인덱스가 배열의 왼쪽 가장자리에 있으면 왼쪽에 요소가 없기 때문에 왼쪽 합계는 0입니다. 이는 배열의 오른쪽 가장자리에도 적용됩니다.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        sumLeft, sumRight = 0, numsSum
        for i in range(len(nums)):
            sumRight -= nums[i]
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]

        return -1
