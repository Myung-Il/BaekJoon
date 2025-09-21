from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node, start, end):
    if start==end:tree[node] = 1
    else:
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def search(node, start, end, find):
    tree[node] -= 1
    if start==end:return end
    mid = (start+end)//2
    return search(node*2, start, mid, find)if tree[node*2]>=find else search(node*2+1, mid+1, end, find-tree[node*2])


n, k = map(int,input().split())
l = [idx+1 for idx in range(n)]
tree = [0]*n*4

init(1, 1, n)
result = []
pin = k

print('<', end='')
for _ in range(n):
    result.append(search(1, 1, n, pin))
    pin = pin+k-1
    while tree[1]and pin>tree[1]:pin -= tree[1]
print(*result, sep=', ', end='>')