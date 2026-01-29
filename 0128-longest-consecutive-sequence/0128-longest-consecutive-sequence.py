"""
어떻게 Set을 사용해서 구현할 수 있지? 연속 구간을 어떻게 활용할 수 있는가?

Set에다가 nums값을 다 넣는다. nums를 돌며, num에 있는 값 + 1이 Set에 있는지 계속 탐색한다.
- 계속해서 있는지 탐색한다면 비효율적이지 않을까? (이미 체크한값 다시 체크)
    - 예: 1,2,3,4를 이미 체크했는데, num=2라면 2부터는 다시 체크할 필요 X

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        num_set = set(nums)
        ans = 1

        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                while num + 1 in num_set:
                    count += 1
                    num += 1

                ans = max(ans, count)

        return ans
