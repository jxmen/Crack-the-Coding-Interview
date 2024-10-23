class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = []
        combinations = []

        def backtrack(start):
            if len(numbers) == k:
                combinations.append(numbers[:])
                return
            
            for i in range(start, n+1):
                numbers.append(i)
                backtrack(i + 1)
                numbers.pop()
        
        backtrack(start=1)
        return combinations
