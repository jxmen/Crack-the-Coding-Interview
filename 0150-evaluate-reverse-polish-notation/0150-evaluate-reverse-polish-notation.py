class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # 토큰을 다 돌린다. 연산자를 만나면 스택에서 숫자 2개를 연산한 값을 다시 넣는다. 스택에 맨 마지막에 남은 하나의 값을 리턴한다.

        operations = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(token)
            elif token == '+':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 + num2)
            elif token == '-':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 - num2)
            elif token == '*':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 * num2)
            elif token == '/':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(int(num1 / num2))
        
        return int(stack[0])
