class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        
        # nums2를 기준으로 단조 감조 스택을 수행하고, 다음 큰 수를 해시맵에 저장한다.
        next_greater_map = {}
        s = []
        for i in range(len(nums2)):
            num = nums2[i]
            if not s or nums2[s[-1]] > num:
                s.append(i) # 인덱스임!!
            else:
                t = s.pop()
                next_greater_map[nums2[t]] = num
                s.append(i)
        
        print(next_greater_map)
        for num in nums1:
            if num not in next_greater_map:
                r.append(-1)
            else:
                r.append(next_greater_map[num])

        return r
        