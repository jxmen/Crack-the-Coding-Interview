def solution(name, yearning, photo):
    n = len(name)
    dict = {}
    for i in range(n):
        dict[name[i]] = yearning[i]

    answer = []
    for lst in photo:
        cnt = 0
        for a in lst:
            if a in dict:
                cnt += dict[a]
        answer.append(cnt)
    return answer
