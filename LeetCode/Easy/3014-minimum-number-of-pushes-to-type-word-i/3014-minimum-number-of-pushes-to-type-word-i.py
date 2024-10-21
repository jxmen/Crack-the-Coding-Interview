class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0
        for char in list(word):
            answer += (answer // 8) + 1
        
        return answer
