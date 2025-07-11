n, m = map(int, input().split())
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    
    # i번 바구니부터 j번 바구니까지 k번 번호를 넣는다.
    for idx in range(i-1, j):
        basket[idx] = k

print(' '.join(map(str, basket)))
