from typing import List



class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # asteroid가 음수일때만 진행한다.
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack

    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        def absolute_value(aInt: int) -> int:
            if aInt < 0:
                return aInt * -1
            else:
                return aInt

        def same_direction(peek: int, ast: int) -> bool:
            if (peek < 0 and ast < 0) or (peek > 0 and ast > 0):
                return True
            else:
                return False
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
                continue

            peek = stack[-1]
            if same_direction(peek, asteroid):
                stack.append(asteroid)
                continue

            if absolute_value(peek) == absolute_value(asteroid):
                stack.pop()
                continue

            while len(stack) != 0 and absolute_value(asteroid) > absolute_value(stack[-1]) and not same_direction(asteroid, stack[-1]):
                stack.pop()

            if len(stack) == 0 or same_direction(asteroid, stack[-1]):
                stack.append(asteroid)

        return stack