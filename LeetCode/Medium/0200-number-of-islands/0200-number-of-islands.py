class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        def visit(x, y, visited):
            visited[x][y] = 1

            # 상하좌우로 이동하면서 반복한다.
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and not visited[nx][ny]:
                    visit(nx, ny, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    visit(i, j, visited)
                    count += 1

        return count
