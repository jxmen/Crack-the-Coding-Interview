from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]):
        def compare(a, b):
            # [3, 30]이 나오면 303이 아닌 330이 나와야 함
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))
        answer = ''
        zeros = 0
        for num in nums_str:
            if num == '0':
                zeros += 1
                continue
            answer += num

        while zeros > 0:
            answer += '0'
            zeros -= 1
        
        return answer if int(answer) != 0 else "0"
