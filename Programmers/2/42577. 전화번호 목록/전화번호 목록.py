def solution(phone_book):
    if len(phone_book) == 1:
        return False

    phones = set(phone_book)
    for phone in phone_book:
        prefix = ""
        for char in phone:
            prefix += char
            if prefix in phones and prefix != phone:
                return False

    return True
