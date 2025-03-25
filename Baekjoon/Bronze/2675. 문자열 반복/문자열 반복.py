# 문자열 S를 입력 받은 후 / 각 문자를 R번 반복해 / P를 만든 후 출력

T = int(input()) # 테스트 케이스 개수
answers = []

for _ in range(T):
    user_input = input()
    R = int(user_input[0])
    S = user_input[2:]

    answer = ''
    for char in list(S):
        answer += char * R

    answers.append(answer)


for answer in answers:
    print(answer)
