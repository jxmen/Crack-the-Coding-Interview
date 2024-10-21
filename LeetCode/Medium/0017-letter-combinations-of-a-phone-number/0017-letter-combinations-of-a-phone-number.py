class Solution:

    """
    백트래킹을 사용한 풀이
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = phone[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations

    """
    처음 백트래킹을 사용하지 않고 반복문으로 푼 함수
    """
    def letterCombinations2(self, digits: str) -> List[str]:
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
