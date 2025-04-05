from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):
    global id, count
    id += 1
    visit[cur] = check = id
    stack.append(cur)
    for nx in graph[cur]:
        if not visit[nx]:check = min(check, scc(nx))
        if visit[nx]:    check = min(check, visit[nx])

    if check==visit[cur]:
        while True:
            node = stack.pop()
            visit[node] = n*2
            group[node] = count
            if cur==node:break
        count += 1
    return check

def notELM(node):return -node


n, m = map(int,input().split())
graph = [[]for _ in range(n*2+1)]
for _ in range(m):
    a, rb1, b, rb2, c, rb3 = input().split()
    a, b, c = map(int, [a, b, c])
    if rb1=="B": a = -a # B = False
    if rb2=="B": b = -b
    if rb3=="B": c = -c
    graph[notELM(a)].append(b) # a -> b
    graph[notELM(a)].append(c) # a -> c
    graph[notELM(b)].append(a)
    graph[notELM(b)].append(c)
    graph[notELM(c)].append(a)
    graph[notELM(c)].append(b)

id, count = 0, 1
visit = [0] * (n*2+1)
group = [0] * (n*2+1)
stack = []
for elm in range(-n, n+1):
    if not elm:continue
    if not visit[elm]:scc(elm)

result = ""
for idx in range(1, n+1):
    if group[idx]==group[-idx]:
        print(-1)
        break
    if group[idx] < group[-idx]:
        result += "R"
    else:result+= "B"
else:print(*result, sep="")

'''
3 R 5 R 6 B
1 B 2 B 3 R
4 R 5 B 6 B
5 R 6 B 7 B
1 R 2 R 4 R

0 1 2 3 4 5 6 7
1     R   R B
2 B B R
3       R B B
4         R B B
5 R R   R
= R B R R B B B
'''