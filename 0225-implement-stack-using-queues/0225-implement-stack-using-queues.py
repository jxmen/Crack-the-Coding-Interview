from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # 비어있는 큐에 먼저 새 요소를 넣고, 원래 큐에 있던 원소를 이동시킨다.

        if not self.q1:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        return not self.q1 and not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
