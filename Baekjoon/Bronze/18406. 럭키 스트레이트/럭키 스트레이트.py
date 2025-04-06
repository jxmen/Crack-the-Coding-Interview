n = int(input())

half = len(str(n)) // 2  # 6일경우 3
l = list(str(n))

leftSum = 0
for left in l[:half]:
    leftSum += int(left)

rightSum = 0
for right in l[half:]:
    rightSum += int(right)

if leftSum == rightSum:
    print("LUCKY")
else:
    print("READY")
