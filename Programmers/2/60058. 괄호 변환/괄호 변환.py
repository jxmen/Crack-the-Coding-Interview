def get_balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i


def is_proper(p):
    stack = []
    for c in list(p):
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False

            stack.pop()

    return len(stack) == 0


# 균형잡힌 문자열: '('와 ')'의 개수가 같아야 함
# 올바른 괄호 문자열: '('와 ')'의 짝도 모두 맞아야 함

def solution(p):
    if p == '':
        return ''

    balanced_index = get_balanced_index(p)
    u, v = p[:balanced_index + 1], p[balanced_index + 1:]
    if is_proper(u):
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'

    u = list(u[1:-1])
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('

        answer += "".join(u[i])

    return answer
