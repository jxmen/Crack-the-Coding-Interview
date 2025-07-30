def solution(n):
    """
    1 -> 1
    2 -> 2
    7 -> 2
    8 -> 3
    13 -> 3
    20 -> 4

    벌집: 육각형
    2 -> 2
    8 -> 3
    20 -> 4
    38 -> 5
    62 -> 6
    """
    
    count = 1
    start = 2

    while start <= n:
        start += (6 * count)
        count += 1

    if start == n:
        return count + 1
    else:    
        return count

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
