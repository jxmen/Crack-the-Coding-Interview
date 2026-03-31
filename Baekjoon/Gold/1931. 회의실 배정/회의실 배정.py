import sys

input = sys.stdin.readline


def solution(n, arr):
    ans = 0
    """
    (끝나는 시간, 시작 시간) 기준으로 정렬한다.
    
    끝나는 시간이 같게 주어진다면 시작 시간이 짧은 것이 우선순위로 주어진다.
    """
    arr.sort(key=lambda x: (x[1], x[0]))

    """
    다음 끝나는 시간에 일치하는 회의를 찾을때 까지 탐욕적으로 탐색한다.
    """
    last_end = 0
    for start, end in arr:
        if start >= last_end:
            ans += 1
            last_end = end

    return ans


if __name__ == '__main__':
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    print(solution(n, arr))
