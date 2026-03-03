class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def helper(image, i, j, color, before_color, visited):
            image[i][j] = color
            visited[i][j] = True

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(image) and 0 <= nj < len(image[0]) and image[ni][nj] == before_color and not visited[ni][nj]:
                    helper(image, ni, nj, color, before_color, visited)

        # dfs로 풀자
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        before_color = image[sr][sc]
        helper(image, sr, sc, color, before_color, visited)
        return image
