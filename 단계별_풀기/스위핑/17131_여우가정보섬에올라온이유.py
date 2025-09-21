from sys import stdin
input = lambda:stdin.readline().strip()
INF = float('inf')


class SegmentTree:
    def __init__(self, N):
        self.arg = [None]*N**3
        self.len = N
    
    def setTree(self, start, end, node):             # 시작지점, 끝지점, 트리 위치
        if start==end:                               # 지점이 확정되면
            self.arg[node] = (star[start][1], start) # 트리에 요소를 저장
            return self.arg[node]                    # 요소와 위치를 반환
        mid = (start+end)//2
        left  = self.setTree(start, mid, node*2)
        right = self.setTree(mid+1, end, node*2+1)

        self.arg[node] = left if left[0]<=right[0]else right
        return self.arg[node]

    def reSetTree(self, start, end, node):
        if self.arg[node]==(INF, INF):return INF, INF
        if start==end:return self.arg[node]

        mid = (start+end)//2
        left  = self.reSetTree(start, mid, node*2)
        right = self.reSetTree(mid+1, end, node*2+1)

        if left[0]<=right[0]:
            self.arg[node] = right
            return right
        else:
            self.arg[node] = left
            return left

    def popElement(self):
        topnode = self.arg[1]
        self.len -= 1
        self.arg[1] = self.reSetTree(0, self.len-1, 1)
        return topnode
    
    def __str__(self):
        return f"{self.arg[:10]}"


n = int(input())
star = [tuple(map(int,input().split()))for _ in range(n)]
tree = SegmentTree(n)

tree.setTree(0, n-1, 1)
print(tree)

print(tree.popElement())
print(tree)