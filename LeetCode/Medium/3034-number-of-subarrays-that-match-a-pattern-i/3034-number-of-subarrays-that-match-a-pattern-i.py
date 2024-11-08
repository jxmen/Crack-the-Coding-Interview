class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # len(pattern) + 1 만큼의 sliding window를 만들고, 밀면서 pattern이 일치하면 +1을 진행한다.

        start, end = 0, len(pattern) + 1
        answer = 0
        subarray = nums[start:end]

        def match_pattern(index, subarray):
            pattern_number = pattern[index]
            if pattern_number == 1 and subarray[index] < subarray[index + 1]:
                return True

            if pattern_number == 0 and subarray[index] == subarray[index + 1]:
                return True

            if pattern_number == -1 and subarray[index] > subarray[index + 1]:
                return True

            return False

        while end <= len(nums):
            subarray = nums[start:end]
            matched = True
            i = 0
            for i in range(len(pattern)):
                if not match_pattern(i, subarray):
                    matched = False
                    break

            if matched:
                answer += 1

            start += 1
            end += 1

        return answer
