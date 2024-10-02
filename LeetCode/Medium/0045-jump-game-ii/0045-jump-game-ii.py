class Solution:

    # 큰거부터 시작하자.
    def jump(self, nums: List[int]) -> int:
        def get_count(start, nums, cache):
            if start in cache:
                return cache[start]
            
            if start >= len(nums) - 1:
                return 0
            
            answer = float('inf')
            for i in range(1, nums[start] + 1):
                if start + i < len(nums):
                    v = get_count(start + i, nums, cache) + 1
                    answer = min(answer, v)
                
            cache[start] = answer
            return answer

        cache={}
        return get_count(start=0, nums=nums, cache=cache)
