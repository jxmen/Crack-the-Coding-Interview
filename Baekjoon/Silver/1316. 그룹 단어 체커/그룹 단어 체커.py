def is_group_word(word):
    """
    aaba -> False
    aab -> True
    ab -> True
    a -> True
    aa -> True
    """
    if not word:
        return True
    
    seen_chars = set()
    current_char = word[0]
    
    for char in word:
        if char != current_char:
            if char in seen_chars:
                return False
            seen_chars.add(current_char)
            current_char = char
    
    return True

def group_word_count(words):
    return sum(1 for word in words if is_group_word(word))

if __name__ == "__main__":
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    result = group_word_count(words)
    print(result)
