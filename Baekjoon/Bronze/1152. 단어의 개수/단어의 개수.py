s = input()

def solution(s):
    return len(
        list(
            filter(lambda x: x != "", s.split(" "))
        )
    )


print(solution(s))

from unittest import TestCase


class Test(TestCase):
    def test1(self):
        self.assertEqual(6, solution("The Curious Case of Benjamin Button"))

    def test2(self):
        self.assertEqual(6, solution(" The first character is a blank"))

    def test3(self):
        self.assertEqual(6, solution("The last character is a blank "))
