from collections import Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                print(num)
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        return list(map(lambda it: it[0], c.most_common(k)))
