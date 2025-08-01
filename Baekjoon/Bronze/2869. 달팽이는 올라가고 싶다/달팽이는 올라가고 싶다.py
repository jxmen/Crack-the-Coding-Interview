"""
높이: v
낮에 a미터 올라감 / 밤에 b미터 미끄러짐

a,b,v = input.split()

접근1: a를 더하고 b를 빼는 것을 v 이상 될때까지 반복 (a를 더해서 이미 v가 된다면 바로 리턴)
접근2: (a-b)한 값을 v에서 나눈 값을 리턴
"""

def solution(a, b, v):
    # 정상에 도달하는 데 필요한 최소 일수 계산
    # 마지막 날에는 밤에 미끄러지지 않으므로, (v - b)까지 올라가면 됨
    # 하루에 (a - b)만큼 올라가고, 올림 처리 필요
    from math import ceil
    return ceil((v - b) / (a - b))


if __name__ == "__main__":
    a, b, v = map(int, input().split())
    print(solution(a, b, v))

