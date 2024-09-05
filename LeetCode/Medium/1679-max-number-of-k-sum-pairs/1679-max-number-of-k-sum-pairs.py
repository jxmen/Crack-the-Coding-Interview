class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1, p2 = 0, len(nums) - 1
        maxOperations = 0

        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                maxOperations += 1
                p1 += 1
                p2 -= 1
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            else:
                p1 += 1
        
        return maxOperations

    # hashMap을 사용해도 풀 수 있다. 이 경우 공간복잡도 최대 N, 시간복잡도도 N 소요(내부 잘못된 로직 수정 필요)
    def maxOperations2(self, nums: List[int], k: int) -> int:
        maxOperations = 0
        hmap = {}

        # 바로 순회하면서 hashmap을 채우는 방식으로 변경이 필요하다.
        for num in nums:
            if not num in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        
        for num in nums:
            if k-num in hmap and hmap[k-num] != 0:
                if k-num == num and hmap[num] == 1:
                    continue
                
                hmap[num] -= 1
                hmap[k-num] -= 1
                maxOperations += 1

        return maxOperations