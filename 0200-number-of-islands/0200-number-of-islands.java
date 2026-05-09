class Solution {
    static int[] dx = new int[]{0, 1, -1, 0};
    static int[] dy = new int[]{1, 0, 0, -1};

    public int numIslands(char[][] grid) {
        int n = grid.length, m = grid[0].length;
        boolean[][] visited = new boolean[n][m];

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    visit(grid, visited, i, j);
                    count++;
                }
            }
        }

        return count;
    }

    private void visit(char[][] grid, boolean[][] visited, int x, int y) {
        int n = grid.length, m = grid[0].length;
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            
            if (
                (0 <= nx && nx < n) 
                && (0 <= ny && ny < m) 
                && !visited[nx][ny] 
                && grid[nx][ny] == '1'
            ) {
                visit(grid, visited, nx, ny);
            }
        }
    }
}
