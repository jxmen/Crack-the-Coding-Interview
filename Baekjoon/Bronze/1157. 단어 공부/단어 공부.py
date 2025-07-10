def solution(s):
    """
    대소문자 구분 X

    Mississipi -> ?
    zZa -> Z
    """

    s = s.lower()

    # 해시맵을 만들고, 카운트한다.
    char_map = {}
    for c in list(s):
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] += 1

    max_count = max(char_map.values())
    if list(char_map.values()).count(max_count) >= 2:
        return '?'

    for k, v in char_map.items():
        if v == max_count:
            return k.upper()
    
    raise RuntimeError("Illegal state exception")

if __name__ == "__main__":
    s = input()
    print(solution(s))
