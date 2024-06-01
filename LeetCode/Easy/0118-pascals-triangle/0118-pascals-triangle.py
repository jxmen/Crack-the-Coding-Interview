class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []

        for i in range(numRows):
            before = []
            if len(rows) > 0:
                before = rows[-1]

            row = [1] * (i + 1) # 1로 먼저 다 채우고 양 끝쪽이 아닌 값들은 새로 값을 할당한다.
            mid = i // 2 + 1
            for j in range(1, mid):
                row[j] = before[j-1] + before[j]
                row[i-j] = row[j] # 대칭 구조이므로 반대편도 같은 값으로 채워준다. [1,4,1,1,1] -> [1,4,1,4,1]
            
            rows.append(row)

        return rows
