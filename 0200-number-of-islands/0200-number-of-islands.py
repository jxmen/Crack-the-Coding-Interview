class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(grid, i, j, visited):
            visited[i][j] = True

            # 상하좌우 움직임을 direction으로 정의해서 순회한다.
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1" and not visited[ni][nj]:
                    visit(grid, ni, nj, visited)

        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    visit(grid, i, j, visited)
                    ans += 1

        return ans
