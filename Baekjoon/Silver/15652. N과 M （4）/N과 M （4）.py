n, m = map(int, input().split())

def backtrack(n, m, path, result):
    if len(path) == m:
        result.append(path[:])
        return

    for i in range(1, n+1):
        if len(path) > 0 and path[-1] > i:
            continue

        path.append(i)
        backtrack(n, m, path, result)
        path.pop()


result = []
backtrack(n, m, [], result)
for nums in result:
    print(' '.join(map(str, nums)))
