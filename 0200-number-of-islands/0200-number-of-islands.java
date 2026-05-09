class Solution {
    static int[][] directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};

    public int numIslands(char[][] grid) {
        int n = grid.length, m = grid[0].length;
        boolean[][] visited = new boolean[n][m];

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    visit(grid, visited, i, j, n, m);
                    count++;
                }
            }
        }

        return count;
    }

    private void visit(char[][] grid, boolean[][] visited, int x, int y, int n, int m) {
        visited[x][y] = true;

        for (int[] d: directions) {
            int nx = d[0] + x, ny = d[1] + y;
            if (
                (0 <= nx && nx < n) && (0 <= ny && ny < m) 
                && !visited[nx][ny] && grid[nx][ny] == '1'
            ) {
                visit(grid, visited, nx, ny, n, m);
            }
        }
    }
}
