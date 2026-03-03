class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for r in zero_rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        for c in zero_cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0


    def setZeroes2(self, matrix: List[List[int]]) -> None:

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
