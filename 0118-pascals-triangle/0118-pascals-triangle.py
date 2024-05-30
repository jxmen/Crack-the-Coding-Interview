class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []

        for i in range(numRows):
            before = []
            if len(rows) > 0:
                before = rows[i-1]

            row = self.get_current_row(i+1, before)
            rows.append(row)

        return rows

        
    def get_current_row(self, n: int, before: List[int]) -> List[int]:
        if n == 1:
            return [1]
        
        if n == 2:
            return [1, 1]
        
        row = []
        for i in range(0, n):
            if i == 0 or i == n-1:
                row.append(1)
                continue
            
            row.append(before[i-1] + before[i])
        
        return row
            

        
