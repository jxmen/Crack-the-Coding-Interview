class Solution:

    # 정석 풀이
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        k = 2 # 중복된 값을 덮어씌울 위치
        for i in range(2, len(nums)):
            
            # 중복을 최대 2개까지만 허용하므로, k-2 값이 다를 경우에만 덮어씌운다.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i] # 덮어씌우기 
                k += 1 # 덮어씌울 위치 이동
        
        return k

    def removeDuplicates2(self, nums: List[int]) -> int:
        n = len(nums)

        p1, p2 = 0, 1
        # 1. 중복되는게 3개 이상 있다면, None으로 바꾼다.
        # [1,1,1,2] -> [1,1,_,2]
        while p2 < n:
            while p2 < n and nums[p1] == nums[p2]:
                if p2 - p1 > 1:
                    nums[p2] = None
                p2 += 1

            p1 = p2


        # 2. array를 한번 더 순회하고, None일 경우 다음 숫자를 찾고 swap한다.
        # [1,1,_,2] -> idx 2,3 swap -> [1,1,2,_]
        p1, p2 = 0, 0
        while p2 < n:
            if nums[p2] is not None:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1

        return p1
