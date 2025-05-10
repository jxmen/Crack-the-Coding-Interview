def recursion(s, l, r, cnt=1):
    if l >= r:
        return [1, cnt]
    elif s[l] != s[r]:
        return [0, cnt]

    return recursion(s, l+1, r-1, cnt+1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
strings = [input() for _ in range(n)]

for i in range(n):
    result, count = is_palindrome(strings[i])
    print(result, count)
