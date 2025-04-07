# 1개 -> 2개 -> 3개 ... 늘려가면서 가장 짧은 문자를 찾자.

"""
aabbcc -> ['a', 'a', 'b', 'b', 'c', 'c']
2개씩 처리한다면, 앞에 2개부터 잘라서 중복된다면 그만큼 숫자를 붙인다. (1개라면 생략)

[aa, bb, cc] -> 2a2b2c

--
pointer를 0부터 시작한다. 그리고 현재 pointer~pointer+length 만큼의 문자를 기억한다. (예: a, aa)
뒤에 값이 같다면 counter를 증가시킨다. 그리고 다른 문자를 만났다면, 새 문자에 숫자와 문자를 같이 더한다.
이를 pointer가 target의 길이가 끝날때까지 반복한다.

length = 1
aabbcc
count, pointer = 1, 0
"""

def zip_string(slice_length, target):
    """
    문자열을 압축한다.
    
    slice_length: 자를 문자열 길이
    target: 압축할 문자
    """
    
    sliced_target = []
    for i in range(0, len(target), slice_length):
        sliced_target.append(target[i:i+slice_length])
    
    new_string = ''
    count, pointer = 1, 0
    while pointer < len(sliced_target):
        count = 1
        while pointer < len(sliced_target) - 1 and sliced_target[pointer] == sliced_target[pointer + 1]:
            count += 1
            pointer += 1
        
        if count > 1:
            new_string += str(count)
        new_string += sliced_target[pointer]
        pointer += 1
    
    return new_string
    

def solution(s):
    if len(s) == 1:
        return 1

    answer = float("inf")
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, len(zip_string(i, s)))
    
    return answer