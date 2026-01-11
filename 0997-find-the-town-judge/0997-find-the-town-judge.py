class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 단방향 그래프를 만든다 -> 그래프 불필요!!
        # graph = [[] for _ in range(n+1)]

        # in: 들어오는, out: 나가는(방향을 가리키는)
        in_degree, out_degree = [0] * (n+1), [0] * (n+1)

        for u, v in trust:
            # graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1
            
        # 1~n까지 out/in 개수 체크
        for i in range(1, n+1):

            # 자신을 제외한 모든 사람이 다 들어오고(in), 나가는(out) 수가 없어야 함
            if in_degree[i] == (n-1) and out_degree[i] == 0:
                return i

        return -1
