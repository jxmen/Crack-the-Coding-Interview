from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # 3x3 영역 안에서 행,열,대각선의 합이 모두 같은 sub grid의 개수를 구하라.
        if len(grid) < 3 or len(grid[0]) < 3: return 0

        # sliding window의 행렬 버전 같은 느낌..
        # (0,0)부터 시작해서, 오른쪽까지 이동하고 만족하면 count를 증가시킨다.
        # 해당 열에서 다 검사했다면 다음 열을 다시 검사한다.

        # 일단 그냥 3x3 grid에서 어떻게 합이 모두 동일한지 판단하는걸 해보자.
        # subGrid 목록들을 만들고 만족하는 개수를 카운트한다.
        count = 0

        # for문으로 sub grid 모두 검사
        for j in range(len(grid) - 2):
            for i in range(len(grid[0]) - 2):
                subGrid = [row[j:j+3] for row in grid[i:i+3]]
                if self.isMagicGrid(subGrid):
                    count += 1

        return count


    def isMagicGrid(self, grid: List[List[int]]) -> bool:
        if len(grid) < 3 or len(grid[0]) < 3: return False

        # check range
        nums = [grid[i][j] for i in range(3) for j in range(3)]
        if sorted(nums) != list(range(1, 10)): return False

        s = sum(grid[0])

        # 가로가 모두 같은가
        for row in grid:
            if s != sum(row):
                return False

        # 세로가 모두 같은지 확인
        colSum = 0
        for i in range(len(grid[0])):
            thisColSum = sum([grid[0][i], grid[1][i], grid[2][i]])
            if s != thisColSum:
                return False

        # 대각선이 같은지 확인
        a = sum([grid[0][0], grid[1][1], grid[2][2]])
        b = sum([grid[2][0], grid[1][1], grid[0][2]])
        return a == s and b == s
