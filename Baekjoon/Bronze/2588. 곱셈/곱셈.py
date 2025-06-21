def solution(n, m):
    nums = []
    
    # m을 1의 자리부터 n을 곱한 값을 nums에 담는다.
    while m > 0:
        # 472에서 2를 구한다.
        m_end_num = m % 10
        num = m_end_num * n
        nums.append(num)
        
        m //= 10

    nums.append(sum(
        [pow(10, i) * nums[i] for i in range(len(nums))])
    )
    return nums

n = int(input())
m = int(input())

nums = solution(n, m)
for num in nums:
    print(num)