import sys

input = sys.stdin.readline


def solution(n, arr):
    max_len = max(list(map(lambda x: len(x), arr)))
    for i in range(n):
        s = arr[i]
        if len(s) < max_len:
            empty_len = max_len - len(s)
            empty_string = ' ' * empty_len
            arr[i] = s + empty_string

    ans = ''
    for i in range(max_len):
        for j in range(n):
            if arr[j][i] != ' ':
                ans += arr[j][i]

    return ans


if __name__ == '__main__':
    n = 5
    arr = [str(input()).replace('\n', '') for _ in range(n)]
    print(solution(n, arr))
