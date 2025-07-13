def solution(n):
    """
    0 -> 4
    1 -> 9
    2 -> 25
    3 -> 
    """
    
    side_length = 3
    # 변 사이마다 + 정사각형 가운데에 점을 하나씩 찍는다.

    for i in range(n-1):
        # 변 길이는 기존 길이 -1 만큼 추가로 더한다.
        side_length += (side_length - 1)

    return pow(side_length, 2)

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
