n, m = map(int, input().split())
nums = list(map(int, input().split()))

def solution(nums, m):
    max_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] <= m:
                    max_sum = max(max_sum, nums[i] + nums[j] + nums[k])

    return max_sum

print(solution(nums, m))
