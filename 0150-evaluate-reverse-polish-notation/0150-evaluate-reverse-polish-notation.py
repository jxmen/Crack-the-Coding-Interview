import operator # 파이썬 표준 라이브러리

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation_map = {
            '+': operator.add, # lambda a,b와 같음
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b), # truncates toward zero
        }

        for token in tokens:
            if token not in operation_map:
                stack.append(int(token))
                continue

            num2, num1 = stack.pop(), stack.pop()
            stack.append(operation_map[token](num1, num2))
        
        return stack[0]


    def evalRPN_with_lambda(self, tokens: List[str]) -> int:
        # 토큰을 다 돌린다. 연산자를 만나면 스택에서 숫자 2개를 연산한 값을 다시 넣는다. 스택에 맨 마지막에 남은 하나의 값을 리턴한다.
        stack = []
        operation_map = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b), # truncates toward zero
        }
        
        for token in tokens:
            if token not in operation_map:
                stack.append(int(token))
                continue

            num2, num1 = stack.pop(), stack.pop()
            stack.append(operation_map[token](num1, num2))
        
        return stack[0]
