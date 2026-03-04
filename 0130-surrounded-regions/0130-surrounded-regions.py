class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # 가장자리를 모두 돌면서, 이어진 'O' 들은 모두 'S' 처리한다.
        def dfs(i, j):
            visited[i][j] = True
            if board[i][j] != 'O':
                return
            
            board[i][j] = 'S'
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == 'O':
                    dfs(ni, nj)

        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]

        # 가장자리 모두 돌면서 이어진 지역은 'S' 처리
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        # 전체 보드 돌면서 값 갱신. 둘러싸인 경우 X처리, 가장자리는 다시 'O'로 변경
        for i in range(n):
            for j in range(m):                
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        
        