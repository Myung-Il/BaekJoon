from sys import stdin
input = lambda:stdin.readline().rstrip()
MAX = 2**21


def search(node, start, end, flag):
    tree[node] -= 1          # 방문 확인
    if start==end:return end # 말단 도착시 번호 확인
    mid = (start+end)//2
    return search(node*2, start, mid, flag)if tree[node*2]>=flag else search(node*2+1, mid+1, end, flag-tree[node*2])
           # tree[node*2]>=flag -> 왼쪽에 있는가
           # flag-tree[node*2]) -> 오른족에 있기 때문에 왼쪽만큼 이동한 것을 없애야한다

def update(node, start, end, flag):
    if flag<start or end<flag:return   # 갱신 범위 초과시 탈출
    tree[node] += 1                    # 방문 기록
    if start==end:return               # 말단 도착시 탈출
    mid = (start+end)//2               #
    update(node*2, start, mid, flag)   #
    update(node*2+1, mid+1, end, flag) #


n = int(input())
l = [idx for idx in range(n)]
tree = [0]*MAX*4
# 입력되는 수의 범위를 알기만 하니 미리 만들어준다

for _ in range(n):
    option, elm = map(int,input().split())
    if option-1:print(search(1, 1, MAX, elm))
    else:update(1, 1, MAX, elm)