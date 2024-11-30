from sys import stdin
input = lambda:stdin.readline().rstrip()


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.left, self.right = None, None


n, k = map(int,input().split())
l = [Node(elm+1) for elm in range(n)]
for idx in range(n):
    l[idx-1].left  = l[idx-2]
    l[idx-1].right = l[idx]

result = []
elm = l[-1]
while elm!=elm.right:
    for _ in range(k):elm = elm.right
    elm.left.right = elm.right
    elm.right.left = elm.left
    result.append(elm.idx)

print('<', end='')
print(*result, sep=', ', end='>')