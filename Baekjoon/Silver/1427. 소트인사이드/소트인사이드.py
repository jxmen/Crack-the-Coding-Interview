str_num = input()

str_num = list(map(int, list(str_num)))
str_num.sort(reverse=True)

for num in str_num:
    print(num, end='')
