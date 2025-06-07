def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

def get_count(num, nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > num:
            end = mid - 1
        elif nums[mid] < num:
            start = mid + 1
        else:
            # 전체 개수를 찾아 리턴한다.
            return upper_bound(nums, nums[mid]) - lower_bound(nums, nums[mid])

    return 0

n = int(input())
card_nums = list(map(int, input().split()))
assert len(card_nums) == n
card_nums.sort()

m = int(input())
nums = list(map(int, input().split()))
assert len(nums) == m

result = []
for num in nums:
    count = get_count(num, card_nums)
    result.append(count)

print(' '.join(map(str, result)))