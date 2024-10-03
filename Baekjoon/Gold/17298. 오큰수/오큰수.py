n = int(input()) # 4
data = list(map(int, input().split())) # 3 5 2 7

# output: 5 7 7 -1

answer = [-1] * n
stack = []
for i in range(len(data)):
    while stack and data[stack[-1]] < data[i]:
        p = stack.pop()
        answer[p] = data[i]
    stack.append(i)

# NOTE: 이미 -1로 초기화되어 있어 이 로직은 필요 없음
while stack:
    p = stack.pop()
    answer[p] = -1

for num in answer:
    print(num, end=' ')

