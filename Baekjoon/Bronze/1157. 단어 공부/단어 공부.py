from collections import Counter

def solution(s):
    """
    대소문자 구분 X

    Mississipi -> ?
    zZa -> Z
    """
    s = s.lower()
    counts = Counter(s)
    max_count = max(counts.values())
    most_common = [char for char, cnt in counts.items() if cnt == max_count]
    if len(most_common) > 1:
        return '?'
    return most_common[0].upper()

if __name__ == "__main__":
    s = input()
    print(solution(s))
