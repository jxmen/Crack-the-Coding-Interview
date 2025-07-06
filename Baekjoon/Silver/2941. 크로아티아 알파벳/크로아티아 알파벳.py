def solution(s):
    # 'dz='를 'z='보다 먼저 처리해야 dz=가 d + z=로 분리되지 않는다.
    croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    
    for c in croatian:
        s = s.replace(c, 'A')
    
    return len(s)

if __name__ == "__main__":
    s = input()
    print(solution(s))
