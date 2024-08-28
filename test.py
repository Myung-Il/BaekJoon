def dfs(now, frm):
    print(now)

    for elm in li[now]:
        if visit[elm]and frm!=elm:
            print('No Tree')
            return
        if visit[elm]:continue
        visit[elm] = 1
        dfs(elm, now)
    print('Tree')
    return

li = [[], [2, 6], [1, 3, 4, 5], [2], [2], [2, 6], [1, 5]]
# li = [[], [2, 6], [1, 3, 4, 5], [2], [2], [2, 6], [5]]
visit = [0]*len(li)
visit[1] = 1
dfs(1, 1)