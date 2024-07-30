class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = [False] * len(isConnected)

        def visit(i):
            for j in range(len(isConnected[i])):
                if not visited[j] and isConnected[i][j] == 1:
                    visited[j] = True
                    visit(j)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                visit(i)
                count += 1

        return count
