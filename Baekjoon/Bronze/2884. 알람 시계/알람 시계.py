def solution(h, m):
    if m >= 45:
        return [h, m - 45]
    
    if h != 0:
        return [h - 1, 60 + (m - 45)]
    else:
        return [23, 60 + (m - 45)]

h, m = map(int, input().split())

a, b = solution(h, m)
print(a, b)