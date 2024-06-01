class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        for i in range(n):
            row = grid[i]
            start, end = 0, len(row) - 1

            if row[0] < 0:
                other_row_counts = (n-i)
                count += other_row_counts * len(row)
                break

            while start <= end:
                mid = (start + end) // 2
                if (row[mid] < 0):
                    # mid ~ end까지 개수 추가
                    count += (end - mid) + 1

                    # mid~start까지 음수만 추가
                    mid -= 1
                    while mid >= 0 and row[mid] < 0:
                        count += 1
                        mid -= 1

                    break

                start = mid + 1

        return count