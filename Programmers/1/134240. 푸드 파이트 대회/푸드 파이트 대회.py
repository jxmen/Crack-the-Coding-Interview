def solution(food):
    answer = ''
    cnt = 0
    for f in food:
        answer += str(cnt) * (f//2)
        cnt += 1
    answer = answer + str(0) + answer[::-1]
    return answer
