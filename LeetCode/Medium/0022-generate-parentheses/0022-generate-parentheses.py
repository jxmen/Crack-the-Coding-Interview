class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(open, close, string, answer):
            # n = 3일때 넘어간 경우 '(((('
            if open > n:
                return

            if open == n and close == n:
                answer.append(string)
                return
            
            backtrack(open + 1, close, string + '(', answer)
            if open > close:
                backtrack(open, close + 1, string + ')', answer)
            
        backtrack(open = 0, close = 0, string = '', answer = answer)
        return answer