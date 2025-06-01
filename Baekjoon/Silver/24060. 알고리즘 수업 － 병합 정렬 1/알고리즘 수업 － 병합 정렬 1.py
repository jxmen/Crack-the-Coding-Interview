a, k = map(int, input().split())
nums = input().split()
assert len(nums) == a

save_count = 0
result = -1

def merge_sort(nums, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        merge(nums, start, mid, end)

def merge(nums, start, mid, end):
    global save_count, result, k

    temp = []
    i, j = start, mid + 1

    # nums[start:mid]와 nums[mid+1:end] 까지 2개의 배열은 정렬되어 있다.
    while i <= mid and j <= end:
        if int(nums[i]) <= int(nums[j]):
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    # 혹시 값이 남아있다면, temp에 추가로 또 저장한다.
    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= end:
        temp.append(nums[j])
        j += 1

    # 저장 횟수를 기록한다.
    for i in range(len(temp)):
        # 시작한곳 부터 값을 다시 써야한다. 그래서 start+i를 해준다.
        nums[start + i] = temp[i]
        save_count += 1
        if save_count == k:
            result = temp[i]

merge_sort(nums, 0, a - 1)

print(result)