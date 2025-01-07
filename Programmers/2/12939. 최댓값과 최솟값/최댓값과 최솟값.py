def solution(s):
    numbers = []
    for number_string in s.split(' '):
        if number_string.startswith('-'):
            numbers.append(int(number_string[1:]) * -1)
        else:
            numbers.append(int(number_string))
    
    return str(min(numbers)) + ' ' + str(max(numbers))