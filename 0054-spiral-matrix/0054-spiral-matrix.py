class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]        
        
        i, j, d = 0, 0, 0
        for _ in range(n * m):
            ans.append(matrix[i][j])
            visited[i][j] = True

            di, dj = directions[d]
            ni, nj = i+di, j+dj

            # 범위 벗어나지 않았다면 회전
            if not (0 <= ni < n and 0 <= nj < m and not visited[ni][nj]):
                d = (d+1) % 4 # 방향 전환
                di, dj = directions[d]
                ni, nj = i+di, j+dj
                
            i, j = ni, nj

        return ans
