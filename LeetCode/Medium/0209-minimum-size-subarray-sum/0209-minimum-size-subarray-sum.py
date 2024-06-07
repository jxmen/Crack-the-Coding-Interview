"""
7 [2 3 1 2 4 3] -> 2
4 [1 4 4] -> 1
11 [1 1 1 1 1 1 1 1] -> 0

0부터 시작해서 target과 같거나 클때 체크한다.
- target과 같을때: subarray의 사이즈가 minLen보다 작다면 minLen을 교체한다.
- target과 클때: 앞에서부터 요소를 하나씩 제거하고, 다시 위의 과정을 거친다.

[2,3,1,2] -> 7보다 큼. 맨 앞에 2 제거
[3,1,2] -> 7보다 작음
[3,1,2,4] -> 7보다 큼. 맨 앞 3 제거
[1,2,4,3]
[2,4,3]
[4,3] -> minLen을 2로 설정

minLen 초기값은 0이다. min(minLen, 2)를 하면 0이 그대로 설정될 것이다. 어떻게 해야할까?
- minLen 설정할때 minLen 값이 0이라면 그냥 2로 덮어씌우자.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        p1, p2 = 0, 0
        n = len(nums)
        currentSum = 0

        while p2 < n:
            currentSum += nums[p2]
            while currentSum >= target:
                minLen = min(minLen, p2 - p1 + 1)
                currentSum -= nums[p1]
                p1 += 1
            p2 += 1

        return minLen if minLen != float('inf') else 0
