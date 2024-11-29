from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node, start, end):
    if start==end:
        tree[node] = [l[start], l[end]]
    else:
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = [tree[node*2][0], tree[node*2+1][1]]
    return tree[node]

def find(node, start, end, mn, mx):
    if start>mx or end<mn:return [float('inf'), 0]
    elif mn<=start and end<=mx:return tree[node]
    mid = (start+end)//2
    left = find(node*2, start, mid, mn, mx)
    right = find(node*2+1, mid+1, end, mn, mx)
    return [min(left[0], right[0]), max(left[1], right[1])]

def update(node, start, end, idx, elm):
    if start>idx or end<idx:pass
    elif start==end:tree[node] = [elm, elm]
    else:
        mid = (start+end)//2
        left = update(node*2, start, mid, idx, elm)
        right = update(node*2+1, mid+1, end, idx, elm)
        tree[node] = [min(left[0], right[0]), max(left[1], right[1])]
    return tree[node]


t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    l = [idx for idx in range(n)]
    tree = [[0, 0]]*n*4
    
    init(1, 0, n-1)
    for _ in range(k):
        ty, a, b = map(int,input().split())
        if ty:print("YES"if find(1, 0, n-1, a, b)==[a, b]else"NO")
        else:
           update(1, 0, n-1, a, l[b])
           update(1, 0, n-1, b, l[a])
           l[a], l[b] = l[b], l[a]