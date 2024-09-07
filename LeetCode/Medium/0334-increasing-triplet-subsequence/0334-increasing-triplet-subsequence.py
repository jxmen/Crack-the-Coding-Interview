class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                # 더 작은 값을 찾았을 경우, first를 업데이트 한다. [10,20,5,30] -> first 10 -> 5, second 20
                # 일시적으로는 i < j < k를 충족하지 않은 상태이지만, second보다 더 큰 값을 찾을 경우 True를 리턴하기 때문에 괜찮다. 
                # first보다 크고 second보다 작은 값을 찾을 경우 second를 업데이트하기 때문인다.
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
