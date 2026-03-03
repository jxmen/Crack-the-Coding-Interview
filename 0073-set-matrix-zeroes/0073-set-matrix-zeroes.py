class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # matrix에서 0인 좌표들을 찾고, 해당 위치를 기억하여 row와 column을 모두 0으로 만든다.

        directions = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    directions.append((i, j))
        
        for d in directions:
            x, y = d
            for i in range(len(matrix)):
                matrix[i][y] = 0
            
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
        