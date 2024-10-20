def solution(s):
    answer = []
    chars = dict()
    
    for i in range(len(s)):
        c = s[i]
        if c not in chars:
            answer.append(-1)
            chars[c] = i
        else:
            answer.append(i - chars[c])
            chars[c] = i
            
    return answer