"""
N마리 중 N/2마리 폰켓몬 가져가기

3 1 2 3 -> 3번 2마리, 1 1마리, 2번 1마리
N = 4, N/2개인 2를 가져가기

1 2 -> 3, 1
1 3 -> 3, 2
1 4 -> 3, 3
2 3 -> 1, 2
2 4 -> 1, 3
3 4 -> 2, 3

map
1 -> 1
2 -> 1
3 -> 1
4 -> 6
"""
def solution(nums):
    dict = {}
    for num in nums:
        if not num in dict:
            dict[num] = 1
        else:
            dict[num] += 1
        
    # 3 3 3 2 2 2 -> min(2, 3)
    types = len(dict) # 포켓몬 종류 개수
    max_take_count = len(nums) // 2 # 가져갈 수 있는 최대 개수
    return min(types, max_take_count)
