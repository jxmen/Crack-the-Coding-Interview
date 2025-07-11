arr = [False] * 30

for _ in range(28):
    num = int(input())
    arr[num-1] = True

for i in range(30):
    if not arr[i]:
        print(i+1)
