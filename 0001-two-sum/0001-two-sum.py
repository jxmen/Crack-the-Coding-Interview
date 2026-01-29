class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. 정렬 + 순회 = O(NlogN)
        2. hashMap에 num-index를 저장하고, nums를 순회 O(N)
            2-0, 7-1, 11-2, 15-3
            for num in nums:
                if (target-num) in map:
                    return [map[num], map[target-num]]
        """
        
        num_indexes = {}
        for i, num in enumerate(nums):
            complement = target - num

            # 찾았다면 바로 리턴
            if complement in num_indexes:
                return [num_indexes[complement], i]
            
            num_indexes[num] = i # 검색 후 추가
        
        return -1
