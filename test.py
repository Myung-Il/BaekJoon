import sys
from math import log2
from collections import deque
 
N=int(sys.stdin.readline())   # 노드 갯수 입력
logN=int(log2(N)+1)           # log
print(logN)
tree=[[] for _ in range(N+1)] # 트리
for _ in range(N-1):
    u,v,w=map(int,sys.stdin.readline().split())
    tree[u].append([v,w]) # u <-w-> v
    tree[v].append([u,w]) # v <-w-> u


p_list=[[0,0] for _ in range(N+1)] # 부모(부모, 댓가) 리스트
depth=[0 for _ in range(N+1)]      # 깊이
p_check=[True for _ in range(N+1)] # 방문
#부모노드 저장
q=deque()   # 덱
q.append(1) # [1]
while q:
    a=q.popleft()       # 부모 노드 꺼내기
    p_check[a]=False    # 방문 기록
    for b,w in tree[a]: # 자식, 댓가
        if p_check[b]:  # 방문 확인
            p_list[b][0]=a # 부모노드 저장
            p_list[b][1]=w # 부모노드까지의 거리 저장
            q.append(b)         # 예제1 [ 1, 2, 4, 5, 3, 6 ]
            depth[b]=depth[a]+1 # 깊이 설정
 
 
#2^k번째 부모 노드와 2^k번째 부모 노드까지의 거리
DP=[[[0,0] for _ in range(logN)] for _ in range(N+1)]
#초기화
for i in range(N+1):
    DP[i][0][0]=p_list[i][0]
    DP[i][0][1]=p_list[i][1]
 
 
#희소테이블 완성하기
for j in range(1,logN):
    for i in range(1,N+1):
        DP[i][j][0]=DP[DP[i][j-1][0]][j-1][0]
        if DP[i][j][0]!=0:
            DP[i][j][1] = DP[i][j-1][1] + DP[ DP[i][j-1][0] ][j-1][1]
 
 
M=int(sys.stdin.readline())
for _ in range(M):
    Q=list(map(int,sys.stdin.readline().split()))
    # 깊이차이
    a=Q[1]
    b=Q[2]
    if depth[a] < depth[b]:
        a, b = b, a
 
    dif = depth[a] - depth[b]
    # 레벨맞추기
    for i in range(logN):
        if dif & 1 << i:
            a = DP[a][i][0]
    if a==b:
        LCA=a
    else:
    #최소공통조상 찾기
        for i in range(logN-1,-1,-1):
            if DP[a][i][0]!=DP[b][i][0]:
                a=DP[a][i][0]
                b=DP[b][i][0]
        #최소공통조상
        LCA = DP[a][0][0]
    #최소공통조상의 레벨
    lca_depth=depth[LCA]
    if Q[0]==1:
        sum = 0
        dif_a=depth[Q[1]]-lca_depth
        dif_b=depth[Q[2]]-lca_depth
        for i in range(logN):
            if dif_a & 1<<i:
                sum +=DP[Q[1]][i][1]
                Q[1]=DP[Q[1]][i][0]
 
            if dif_b & 1<<i:
                sum +=DP[Q[2]][i][1]
                Q[2]=DP[Q[2]][i][0]
        print(sum)
 
    elif Q[0]==2:
        gep=depth[Q[1]]-lca_depth+1
        if Q[3]<=gep:
            for i in range(logN):
                if Q[3]-1 & 1<<i:
                    Q[1]=DP[Q[1]][i][0]
            print(Q[1])
 
        else:
            Q[3] = depth[Q[2]]-Q[3]+depth[Q[1]]-2*lca_depth+1
            for i in range(logN):
                if Q[3] & 1<<i:
                    Q[2]=DP[Q[2]][i][0]
            print(Q[2])