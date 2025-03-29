"""
WA -> 10 + 3
UNUCIC -> (868242) -> 9+7+9+3+5+3 -> 36

문자-숫자 해시맵을 만들고 문자가 없어질때까지 값을 더하자.
A - 2,
B - 2,
C - 2,
D - 3
...
"""
from operator import indexOf

string_number_map = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}

S = input()

def solution(s):
    answer = 0
    while len(s):
        char = s[-1]
        for key, value in string_number_map.items():
            if char in key:
                answer += value

        s = s[:-1]

    return answer


print(solution(S))

# === Test Case

from unittest import TestCase, main


class Test(TestCase):

    def test1(self):
        self.assertEqual(13, solution('WA'))

    def test2(self):
        self.assertEqual(36, solution('UNUCIC'))


if __name__ == '__main__':
    main()
