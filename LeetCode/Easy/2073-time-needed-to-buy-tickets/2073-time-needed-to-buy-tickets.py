from typing import List
from unittest import TestCase


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        n명의 사람들이 티켓을 사기 위해 줄을 서고 있다. 0th 사람은 앞 라인에 있고 n-1th 사람을 뒷라인에 있다
        0-indexed 정수인 n길이의 tickets이 주어진다. i번째 사람이 사고 싶어하는 티켓의 수는 tickets[i]에 위치한다.

        각각의 사람은 1초에 한번만 티켓을 구매할 수 있다. 그리고 한번 구매하면 줄 맨 뒤로 이동해야 한다.

        k번째 인덱스에 속한 사람이 티켓을 모두 구하려면 몇초가 걸리는지 리턴하시오.

        :param tickets:
        :param k:
        :return: k번째 인덱스에 속한 사람이 티켓을 구매하기 위해 걸리는 시간
        """

        # [4,0,0,0] -> 4초

        time = 0
        while tickets[k] > 0:
            # rotate
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return time

                if tickets[i] != 0:
                    tickets[i] -= 1
                    time += 1

        return time


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test(self):
        self.assertEqual(6, self.solution.timeRequiredToBuy([2, 3, 2], 2))

    def test2(self):
        self.assertEqual(8, self.solution.timeRequiredToBuy([5, 1, 1, 1], 0))

    def test3(self):
        self.assertEqual(154, self.solution.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3))
