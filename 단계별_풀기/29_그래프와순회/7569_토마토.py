from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()

r, c, h = map(int,input().split())
box = [[list(map(int,input().split()))for _ in range(c)] for _ in range(h)]
visit= [[[False]*r for _ in range(c)] for _ in range(h)]

d = deque()
for high in range(h):
    for col in range(c):
        for row in range(r):
            if box[high][col][row]==1:
                d.append([high, col, row])

zl = [ 1,-1, 0, 0, 0, 0]
yl = [ 0, 0, 1,-1, 0, 0]
xl = [ 0, 0, 0, 0, 1,-1]
while d:
    z, y, x = d.popleft()
    if visit[z][y][x]:continue
    visit[z][y][x] = True

    for idx in range(6):
        zi, yi, xi = z+zl[idx], y+yl[idx], x+xl[idx]
        if 0<=zi<h and 0<=yi<c and 0<=xi<r:
            if not box[zi][yi][xi]:
                box[zi][yi][xi] = box[z][y][x]+1
                d.append([zi, yi, xi])

for high in range(h):
    for col in range(c):
        for row in range(r):
            if not box[high][col][row]:
                print(-1)
                exit()
print(box[z][y][x]-1)