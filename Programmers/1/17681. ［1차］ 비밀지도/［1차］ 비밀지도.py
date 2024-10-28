"""
2차원 배열을 n만큼 만든다.
arr1, arr2를 해독하여 2차원 배열에 벽을 추가한다.
arr1, arr2의 숫자를 각각 2진수로 변환한다. 2진수로 변환한 값의 길이가 n보다 작다면 앞에는 0이다.
"""

def solution(n, arr1, arr2):
    answer = []
    secret_map = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        num = arr1[i]
        # 2진수로 변환 후 map에 벽 추가
        s = str(bin(num))[2:]
        if len(s) < n:
            m = n - len(s)
            temp = ''
            for _ in range(m):
                temp += '0'
            s = temp + s
        
        for j in range(n):
            char = s[j]
            if char == '1':
                secret_map[i][j] = 1
    
    for i in range(n):
        # 2진수로 변환 후 map에 벽 추가
        num = arr2[i]
        # 2진수로 변환 후 map에 벽 추가
        s = str(bin(num))[2:]
        if len(s) < n:
            m = n - len(s)
            temp = ''
            for _ in range(m):
                temp += '0'
            s = temp + s
        
        for j in range(n):
            char = s[j]
            if char == '1':
                secret_map[i][j] = 1
    
    for numbers in secret_map:
        string = ''
        for number in numbers:
            if number == 1:
                string += '#'
            else:
                string += ' '
        answer.append(string)
    
    return answer
