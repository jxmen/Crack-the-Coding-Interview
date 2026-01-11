class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(graph, visited, s):
            visited.add(s)
            for v in graph[s]:
                if v not in visited:
                    dfs(graph, visited, v)
            
        visited = set()
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # 그래프 탐색
        dfs(graph, visited, source)
        return destination in visited
