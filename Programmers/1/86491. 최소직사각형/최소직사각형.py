def solution(sizes):
    walletSizes = []

    # 큰 것을 가로로, 작은 것은 세로로 설정한다.
    for size in sizes:
        if size[0] < size[1]:
            size[1], size[0] = size[0], size[1]
        
    # 가장 큰 값을 구하고 곱을 리턴한다.
    maxWidth, maxHeight = 0, 0
    for size in sizes:
        maxWidth, maxHeight = max(maxWidth, size[0]), max(maxHeight, size[1])
        
    return maxWidth * maxHeight