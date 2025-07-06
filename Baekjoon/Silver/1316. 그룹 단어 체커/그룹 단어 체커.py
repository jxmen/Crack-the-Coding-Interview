def is_group_word(word):
    """
    aaba -> False
    aab -> True
    ab -> True
    a -> True
    aa -> True
    """

    char_set = set(word[0])
    p = 0
    prev = word[0]

    while p < len(word):
        if word[p] != prev:
            if word[p] in char_set:
                return False

            char_set.add(prev)
            prev = word[p]
        
        p += 1
    
    return True

def group_word_count(words):
    cnt = 0
    for word in words:
        if is_group_word(word):
            cnt += 1

    return cnt

if __name__ == "__main__":
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    result = group_word_count(words)
    print(result)
