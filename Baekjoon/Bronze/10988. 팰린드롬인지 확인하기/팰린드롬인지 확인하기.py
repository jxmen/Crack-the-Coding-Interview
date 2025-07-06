def is_panlindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            return False
    
    return True

if __name__ == "__main__":
    s = input()
    print(1 if is_panlindrome(s) else 0)
