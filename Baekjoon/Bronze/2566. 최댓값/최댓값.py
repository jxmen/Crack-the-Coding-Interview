def solution(matrix):
    max_num, i, j = 0, 0, 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            num = matrix[x][y]
            if num > max_num:
                max_num = num
                i, j = x, y
    
    return [max_num, i+1, j+1]

if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for _ in range(9)]

    max_num, i, j = solution(matrix)
    print(max_num)
    print(i, j)
