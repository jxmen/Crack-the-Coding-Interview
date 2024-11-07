class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        def backtrack(x, y, string, visited):
            if string == word:
                return True

            if not word.startswith(string):
                return False
            
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    result = backtrack(nx, ny, string + board[nx][ny], visited)
                    visited[nx][ny] = False
                    if result == True:
                        return True
            
            return False
        
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                result = backtrack(i, j, board[i][j], visited)
                if result == True:
                    return True
                
                visited[i][j] = False
        
        return False
