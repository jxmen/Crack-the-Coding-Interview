S = input()

def reverse_string(s):
    temp = ""

    while s != "":
        temp += s[-1]
        s = s[:-1]

    return temp

def solution(s):
    num1, num2 = [int(reverse_string(x)) for x in s.split(" ")]

    return max(num1, num2)

print(solution(S))

# === Test Case

from unittest import TestCase, main

class Test(TestCase):
    def test1(self):
        self.assertEqual( 437, solution( "734 893") )

    def test2(self):
        self.assertEqual(132, solution("221 231"))

    def test3(self):
        self.assertEqual(938, solution("839 237"))

if __name__ == '__main__':
    main()
