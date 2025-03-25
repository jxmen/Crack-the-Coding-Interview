S = input()

alphabet_strings = "abcdefghijklmnopqrstuvwxyz"
indexes = []
for alphabet in list(alphabet_strings):
    flag = False
    for i in range(len(S)):
        char = S[i]
        if char == alphabet:
            flag = True
            indexes.append(i)
            break

    if not flag:
        indexes.append(-1)

for index in indexes:
    print(index, end=" ")
