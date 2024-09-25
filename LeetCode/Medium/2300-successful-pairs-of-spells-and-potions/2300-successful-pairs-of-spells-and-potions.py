class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # potions가 정렬되어 있다면 bs를 활용할 수 있을 것 같은데...
        # 완전탐색 -> 최적화

        potions.sort() # Binary Search를 하기 위해 정렬
        pairs = []
        for spell in spells:
            count = 0
            start, end = 0, len(potions) - 1
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] * spell >= success:
                    end = mid - 1
                else:
                    start = mid + 1
            
            pairs.append(len(potions) - start)
        
        return pairs
