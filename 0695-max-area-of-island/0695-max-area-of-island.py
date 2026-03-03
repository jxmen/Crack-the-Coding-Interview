class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visit(x, y):
            visited[x][y] = True

            count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and not visited[nx][ny]:
                    count += visit(nx, ny)

            return count + 1

        ans = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, visit(i, j))

        return ans
