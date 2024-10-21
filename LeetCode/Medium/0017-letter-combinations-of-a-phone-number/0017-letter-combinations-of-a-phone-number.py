class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = dict()
        d[2] = 'abc'
        d[3] = 'def'
        d[4] = 'ghi'
        d[5] = 'jkl'
        d[6] = 'mno'
        d[7] = 'pqrs'
        d[8] = 'tuv'
        d[9] = 'wxyz'
    
        # 한자리씩 지우면서 다시 answer를 만든다. 23의 경우 [a,b,c]가 answer가 되었다가 이 answer로 다시 돌면서 새 answer를 만든다.
        answer = []
        while len(digits):
            top = int(digits[0])
            letters = d[top]
            digits = digits[1:]

            if not len(answer):
                for letter in letters:
                    answer.append(letter)
                continue

            new_answer = []
            for a in answer:
                for letter in letters:
                    new_answer.append(a + letter)

            answer = new_answer
                
        return answer
        