"""
[[1,1,0], [1,1,0], [0,0,1]]

i=0, computer = [1,1,0]
visited: [True, False, False]
computer의 index가 i가 아니고, 방문하지 않은 것들이 이어진 것을 모두 찾는다.
    index 1 방문
    visited: [True, True, False]

i=1, computer = [1,1,0]

    

for i in range(len(computers)):
    computer = computers[i]
    if visited[i] or computer == 0:
        continue
  
    for j in range(len(computer)): # j=0일때 [1,1,0]
        if visited[j] == 1:
            visited[j] = True
            visit()

    answer += 1

"""

def solution(n, computers):
    
    # TODO: visit dfs 처리하기
    def visit(idx, computers, visited):
        for i in range(len(computers[idx])):
            if not visited[i] and computers[idx][i] == 1:
                visited[i] = True
                visit(i, computers, visited)
    
    def dfs(computers, visited, answer):
        for i in range(len(computers)):
            computer = computers[i]
            if visited[i] or computer == 0:
                continue
            
            for j in range(len(computer)): # j=0일때 [1,1,0]
                if computer[j] == 1:
                    visited[j] = True
                    visit(j, computers, visited)

            answer += 1
        
        return answer
        
    return dfs(computers, [False] * len(computers), 0)