class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s, e = 1, num
        while s <= e:
            mid = (s + e) // 2
            if mid ** 2 < num:
                s = mid + 1
            elif mid ** 2 > num:
                e = mid - 1
            else:
                return True
        
        return False
