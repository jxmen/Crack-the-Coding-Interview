from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 처음 위치가 아니고, 다음 위치에서 maze를 벗어난다면 해당 count를 리턴한다.

        steps = 0
        queue = deque([entrance])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # 미로 index를 벗어나지 않고 갈 수 있는 영역인지 체크
                    if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] == '.':

                        # 끝 지점이라면 리턴
                        if ni == 0 or ni == len(maze) - 1 or nj == 0 or nj == len(maze[0]) - 1:
                            return steps + 1

                        queue.append([ni, nj])
                        maze[ni][nj] = '+'
                
            steps += 1
                            
        return -1
