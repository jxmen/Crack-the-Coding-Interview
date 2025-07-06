def solution(n):
    s = ''
    for i in range(0, n, 4):
        s += 'long '
    
    return s + 'int'
    # return ''.join(['long ' for _ in range(0, n, 4)]) + 'int'

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
