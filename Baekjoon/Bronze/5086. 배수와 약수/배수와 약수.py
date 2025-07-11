def solution(a, b):
    if b % a == 0:
        return 'factor'
    elif a % b == 0:
        return 'multiple'
    else:
        return 'neither'
    
if __name__ == "__main__":
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break

        print(solution(a,b))
