from sys import stdin
input = lambda:stdin.readline().strip()

n, d = map(int, input().split())
stone = list(map(int, input().split()))

tree = [0]*(2**len(bin(n)[1:]))
def search(node, left, right, start=0, end=n-1):
    if left<=start and end<=right: return tree[node]
    if end<left or right<start: return 0
    
    mid = (start+end)//2
    lt = search(node*2, left, right, start, mid)
    rt = search(node*2+1, left, right, mid+1, end)
    return max(lt, rt)

def update(node, idx, val, start=0, end=n-1):
    if start==end:
        if start==idx:tree[node] = val
    else:
        mid = (start+end)//2
        update(node*2, idx, val, start, mid)
        update(node*2+1, idx, val, mid+1, end)
        tree[node] = max(tree[node*2], tree[node*2+1])

dp = [-float("inf")]*(n+1)
for i in range(1, n+1):
    dp[i] = max(stone[i-1], stone[i-1]+search(1, i-d, i-1))
    update(1, i, dp[i])

print(max(dp))

...
'''
dp : 문제의 규칙을 찾아 쉽게 해결 할 수 있다.
dq : 슬라이딩 윈도우를 이용해서 뛰어넘을 수 있는 최대 거리를 알 수 있다.
st : 구간의 정의대해서 쉽게 얻을 수 있다.


2 7 -5 -4 10 -5 -5 -5 30 -10 [res]
2====|  |     |  |     |       |
2 9=====|     |  |     |       |
2 9     5=====|  |     |       |
2 9     5 15=====|     |       |
2 9     5 15    10=====|       |
2 9     5 15    10    40====   |
2 9     5 15    10    40     [ 40]


============================
============ ===============
====== ===== ======== ======
=== == == == ===== == == ===
= =  |  |  | == ==  |  |  |
| |  |  |  |  |  |  |  |  |
2 7 -5 -4 10 -5 -5 -5 30 -10
O O  X  O  O  X  O  X  O  X

=======================
========== ============
===== ==== ====== =====
=== = = == === == == ==
= = | |  | = =  |  |  |
| | | |  | | |  |  |  |
2 9 4 0 10 5 0 -5 25 15

============15==============
======10==== ========5======
==4=== ==6== ===-15== ==20==
=9= == == == =-10= == == ===
= =  |  |  | == ==  |  |  |
| |  |  |  |  |  |  |  |  |
2 7 -5 -4 10 -5 -5 -5 30 -10

2 9 X 5 15 X 10 X 40 X

밟으면 안되는 조건이 애매함, 그때 상황에 따라 봐야 됨
최대 값을 찾고 양 옆으로 이동하는 것도 생각해봐야 됨

1. 나만 선택하기: dp[j] + 
'''