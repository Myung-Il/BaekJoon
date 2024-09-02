from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def union(x, y, w):
    x = find(x) # 방문 확인
    y = find(y) # 방문한 적 있다면 조상 노드를 가져옴
    if x==y:return # 이미 방문했다면 굳이 뭘 할 필요가 없음

    if x<y:parents[y] = x # 조상
    if x>y:parents[x] = y # 설정

    global s
    s+=w # 방문한 적 없다면 가중치 +

def find(x): # 조상 노드가 있는지 검사
    if x!=parents[x]:
        parents[x]=find(parents[x])
    return parents[x]


v,e=map(int,input().split())
l=sorted([list(map(int,input().split()))for _ in range(e)],key=lambda x:x[2])
parents=[i for i in range(v+1)] # 가중치를 기준으로 정렬

s = 0
for a, b, w in l:
    union(a, b, w) # 트리 연결
print(s)