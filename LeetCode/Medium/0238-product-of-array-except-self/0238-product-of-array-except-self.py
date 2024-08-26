class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 왼쪽 곱과 오른쪽 곱을 구한 후 다시 서로 곱한다.
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        answer = [0] * n
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer
        