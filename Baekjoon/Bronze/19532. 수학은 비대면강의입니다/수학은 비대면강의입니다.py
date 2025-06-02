a,b,c,d,e,f = map(int, input().split())

"""
연립방정식에서 x와 y값 계산

ax + by = c
dx + ey = f

-999 <= a,b,c,d,e,f <= 999
"""

def calculate(a,b,c,d,e,f):
    for x in range(-999, 1000, 1):
        for y in range(-999, 1000, 1):
            if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
                return [x, y]

    return []

x, y = calculate(a,b,c,d,e,f)
print(x, y)
