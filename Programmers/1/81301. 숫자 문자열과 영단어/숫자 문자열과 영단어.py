"""
set + hashmap

set -> (zero, one, two, ....)
hashmap {
    zero -> 0
    one -> 1
    two -> 2
    ...
}

for number_string in number_strings:
    if s.startswith(number_string):
        answer += number_map[number_string]
        s = s[len(number_string):]

if s[0].isnumber():
    answer += s[0]
    s = s[1:]

"""

def solution(s):
    answer = ''
    
    numbers = set([str(i) for i in range(0, 10)])
    number_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    def is_number(char):
        return char in numbers
    
    # one4seveneight -> 1478
    while len(s):
        for number_string in number_map.keys():
            if s.startswith(number_string):
                answer += number_map[number_string]
                s = s[len(number_string):]
                break
        
        if len(s) and is_number(s[0]):
            answer += s[0]
            s = s[1:]
    
    return int(answer)