n = int(input())

stars, spaces = 1, n-1
for i in range(n):
    spaces = (n - 1) - i
    stars = (2 * i) + 1
    print(' ' * spaces + '*' * stars)

for i in range(n-1):
    spaces = i + 1
    stars = 2 * (n - 1 - i) -1
    print(' ' * spaces + '*' * stars)
