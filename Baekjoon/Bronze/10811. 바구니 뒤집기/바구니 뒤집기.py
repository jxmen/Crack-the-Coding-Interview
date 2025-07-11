def reverse(start, end, basket):
    left, right = start, end
    while left < right:
        basket[left], basket[right] = basket[right], basket[left]
        left += 1
        right -= 1

n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())

    # i번째 바구니부터 j번째 바구니까지 순서를 변경한다.
    reverse(start=i-1, end=j-1, basket=basket)

print(' '.join(map(str, basket)))