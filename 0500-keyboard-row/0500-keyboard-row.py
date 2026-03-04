class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set(list('qwertyuiopQWERTYUIOP')),
            set(list('asdfghjklASDFGHJKL')),
            set(list('zxcvbnmZXCVBNM')),
        ]

        ans = []
        for word in words:
            for row in rows:
                if all(map(lambda x: x in row, list(word))):
                    ans.append(word)

        return ans