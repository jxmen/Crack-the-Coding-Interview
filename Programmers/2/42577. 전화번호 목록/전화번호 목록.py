def solution(phone_book):
    if len(phone_book) == 1:
        return False

    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = 1

    for phone in phone_book:
        prefix = ""
        for char in phone:
            prefix += char
            if prefix in phone_dict and prefix != phone:
                return False

    return True