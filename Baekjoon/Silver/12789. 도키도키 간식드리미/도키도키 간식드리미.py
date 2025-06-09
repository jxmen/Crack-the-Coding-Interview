n = int(input())
nums = list(map(int, input().split()))
assert n == len(nums)

def can_eat_snack(nums):
    stack = []
    current_snack = 1

    for num in nums:
        stack.append(num)

        while stack and stack[-1] == current_snack:
            stack.pop()
            current_snack += 1

    return not stack

print("Nice" if can_eat_snack(nums) else "Sad")

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(can_eat_snack([5,4,1,3,2]))

    def test2(self):
        self.assertFalse(can_eat_snack([4,5,1,3,2]))

    def test3(self):
        self.assertTrue(can_eat_snack([5,4,1,2,3]))

if __name__ == '__main__':
    unittest.main()
