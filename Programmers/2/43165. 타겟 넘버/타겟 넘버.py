def solution(numbers, target):
    def dfs(numbers, target, sum, count):
        if len(numbers) == 0:
            if target == sum:
                return count + 1
            else:
                return count
        
        plus = dfs(numbers[1:], target, sum + numbers[0], count)
        minus = dfs(numbers[1:], target, sum - numbers[0], count)
        
        return plus + minus
        
    return dfs(numbers, target, 0, 0)
