from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque() # 하나만 써도 구현 가능하다.

    def push(self, x: int) -> None:
        self.q.append(x)

        # 기존 요소 재배치
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
