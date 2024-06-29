class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        diff = [[], []]

        # 겹치는건 diff에 넣지 말아야 한다.
        for i in range(len(nums1)):
            if nums1[i] not in nums2Set:
                diff[0].append(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1Set:
                diff[1].append(nums2[i])

        # diff 안 각각 요소 중복 제거
        return map(lambda x: list(set(x)), diff)
