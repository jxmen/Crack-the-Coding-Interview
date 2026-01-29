class Solution:
    def mySqrt(self, x: int) -> int:
        s, e = 0, x
        result = 0
        while s <= e:
            mid = s + (e - s) // 2
            square = mid * mid
            if square <= x:
                result = mid
                s = mid + 1
            else:
                e = mid - 1

        return result
