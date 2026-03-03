def visit(grid, i, j):
    if grid[i][j] == '0':
        return

    # (in-place) visited를 쓰지 않고 기존 값을 0으로 바꾼다
    grid[i][j] = "0"

    # 상하좌우 움직임을 direction으로 정의해서 순회한다.
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            visit(grid, ni, nj)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visit(grid, i, j)
                    ans += 1

        return ans
