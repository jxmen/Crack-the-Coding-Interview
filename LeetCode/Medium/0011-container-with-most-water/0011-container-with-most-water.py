class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        p1, p2 = 0, len(height) - 1

        while p1 <= p2:
            width = p2 - p1
            if height[p1] > height[p2]:
                maxArea = max(maxArea, height[p2] * width)
                p2 -= 1
            else:
                maxArea = max(maxArea, height[p1] * width)
                p1 += 1
        
        return maxArea
        