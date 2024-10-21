class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, numbers):
            if len(numbers) == k:
                if sum(numbers) == n:
                    combinations.append(numbers[:])
                return
            
            for i in range(start, 10):
                numbers.append(i)
                backtrack(i + 1, numbers)
                numbers.pop()
        
        combinations = []
        backtrack(1, [])
        return combinations
