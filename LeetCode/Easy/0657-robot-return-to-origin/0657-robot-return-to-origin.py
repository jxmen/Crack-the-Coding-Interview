class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in list(moves):
            if move == 'U': y += 1
            if move == 'D': y -= 1
            if move == 'L': x -= 1
            if move == 'R': x += 1
        
        return x == 0 and y == 0
