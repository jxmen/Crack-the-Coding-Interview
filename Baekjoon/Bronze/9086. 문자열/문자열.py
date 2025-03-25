n = int(input())

answers = []
for _ in range(n):
    s = input()

    first_char = s[0]
    last_char = s[len(s) - 1]

    answers.append(first_char + last_char)

for answer in answers:
    print(answer)
