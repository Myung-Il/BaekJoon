from collections import deque
from sys import stdin
input=lambda:stdin.readline().rstrip()


def node(x): # 자식 -> 부모:;자식 -> 부모
    l = [x]
    while tree[x]:
        l.append(tree[x])
        x = tree[x]
    return l



t = int(input())
for _ in range(t):
    n = int(input())
    tree = [0]*(n+1)
    for _ in range(n-1):
        a, b = map(int,input().split())
        tree[b] = a # idx:자식, elm: 부모
    
    a, b = map(int,input().split())
    target_a = node(a)
    target_b = node(b)

    target_a_lvl = len(target_a)-1 # 끝은 뿌리이다
    target_b_lvl = len(target_b)-1 # 거기서부터 내려온다면 다른게 있을 것이다
    while target_a[target_a_lvl]==target_b[target_b_lvl]: # 달라진다면 다로 위의 부모 노드가 정답이다
        target_a_lvl -= 1
        target_b_lvl -= 1
    
    print(target_a[target_a_lvl+1])