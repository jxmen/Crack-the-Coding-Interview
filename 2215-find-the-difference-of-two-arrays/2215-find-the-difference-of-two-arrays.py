class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [set(), set()]

        nums1_set, nums2_set = set(nums1), set(nums2)
        for num in nums1:
            if num not in nums2:
                answer[0].add(num)

        for num in nums2:
            if num not in nums1:
                answer[1].add(num)

        answer[0], answer[1] = list(answer[0]), list(answer[1])
        return answer
