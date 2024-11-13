from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        answer = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            answer += up - low
        return answer
