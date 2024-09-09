def dfs(row, visit):
    if row == N:
        return 0

    if visited[visit] != -1:
        return visited[visit]

    ret = 1000000000
    for i in range(N):
        if (visit & (1 << i)) != 0:  # 특정 비트가 켜저있다면
            continue

        ret = min(ret, dfs(row + 1, (visit | (1 << i))) + tasks[row][i])
       
    visited[visit] = ret
    print(row, visit, visited)

    return visited[visit]


N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

visited = [-1] * (1 << N)
print(dfs(0, 0))