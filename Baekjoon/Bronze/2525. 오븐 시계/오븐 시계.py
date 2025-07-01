def solution(h, m, c):
    if m + c < 60:
        return [h, m+c]
    
    total_minutes = m+c
    while total_minutes >= 60:
        h += 1
        total_minutes -= 60

    if h >= 24:
        return [h-24, total_minutes]
    else:
        return [h, total_minutes]

if __name__ == '__main__':
    h, m = map(int, input().split())
    c = int(input())

    result = solution(h, m, c)
    print(result[0], result[1])
