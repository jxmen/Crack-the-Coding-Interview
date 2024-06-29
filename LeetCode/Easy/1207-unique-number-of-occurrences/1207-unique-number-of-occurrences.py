class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numMap = {}
        for num in arr:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] = numMap[num] + 1
        
        numCountSet = set()
        for count in numMap.values():
            if count in numCountSet:
                return False
            
            numCountSet.add(count)
            
        return True
