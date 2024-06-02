def solution(t, p):
    # 1. sliding window로 구현
    # len(t) = 7, len(p) = 3 일때 loop가 5까지 돌아야 함 (7-3) + 1 = 5

    answer, tStart = 0, 0
    while tStart <= len(t) - len(p):
        sliced = t[tStart:tStart + len(p)]
        if int(sliced) <= int(p):
            answer += 1

        tStart += 1

    return answer


import unittest


class UnitTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(solution(t="3141592", p="271"), 2)

    def testcase2(self):
        self.assertEqual(solution(t="500220839878", p="7"), 8)

    def testcase3(self):
        self.assertEqual(solution(t="10203", p="15"), 3)
