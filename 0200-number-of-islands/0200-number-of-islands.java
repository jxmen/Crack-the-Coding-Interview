class Solution {


    public int numIslands(char[][] grid) {
        int n = grid.length, m = grid[0].length;

        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }

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

    private void visit(char[][] grid, boolean[][] visited, int i, int j) {
        int n = visited.length, m = visited[0].length;
        visited[i][j] = true;
        
        // TODO: 상하좌우 모두 영역을 넘지 않고 1이라면, 또 visit 처리
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, 1, -1, 0};

        for (int k = 0; k < 4; k++) {
            int nx = dx[k] + i;
            int ny = dy[k] + j;
            
            if ((0 <= nx && nx < n) && (0 <= ny && ny < m) && !visited[nx][ny] && grid[nx][ny] == '1') {
                visit(grid, visited, nx, ny);
            }
        }
    }
}