n = int(input())
nums = list(map(int, input().split()))

def solution(nums):
    """
    수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

    예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
    """

    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):

        # 이전 수를 다 뒤져서 이어 붙일 수 있는 만큼 숫자에서 +1을 한다.
        max_dp = 0
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            
    return max(dp)

print(solution(nums))
