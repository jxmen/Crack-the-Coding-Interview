def solution(nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == mid:
            return nums[mid]
        elif nums[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1

    return -1

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]

    print(solution(nums))

