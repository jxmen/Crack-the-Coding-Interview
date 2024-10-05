def solution(numbers, target):
    def dfs(numbers, target, count):
        if len(numbers) == 0:
            return count + 1 if target == 0 else count
            
        plus = dfs(numbers[1:], target - numbers[0], count)
        minus = dfs(numbers[1:], target + numbers[0], count)
        
        return plus + minus
        
    return dfs(numbers, target, 0)
