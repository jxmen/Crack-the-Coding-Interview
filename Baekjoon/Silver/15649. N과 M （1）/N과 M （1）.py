n, m = map(int, input().split())

def backtrack(n, m, path, visited, result):
    if len(path) == m:
        result.append(path[:])
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        path.append(i)
        backtrack(n, m, path, visited, result)
        path.pop()
        visited[i] = False


result = []
visited = [False] * (n+1)
backtrack(n, m, [], visited, result)
for nums in result:
    print(' '.join(map(str, nums)))
