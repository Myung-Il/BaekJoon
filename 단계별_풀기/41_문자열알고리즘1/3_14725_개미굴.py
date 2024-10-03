from sys import stdin
input=lambda:stdin.readline().rstrip()


class Trie:
    def __init__(self) -> None:
        self.r00t = {}       # 조상 노드

    def insert(self, child): # 자식 노드
        cur = self.r00t      # 부모 설정

        for kid in child:      # 자식을 하나씩 받기
            if kid not in cur: # 부모에 자식이 없다면
                cur[kid] = {}  # 자식을 추가
            cur = cur[kid]     # 추가된 자식을 부모로 다시 설정
        cur[0] = True          # 끝에 도착 했음을 기록

    def tree(self, lvl, cur):   # 현재 층과 부모를 설정
        if 0 in cur:return      # 층이 끝에 도달했다면 그냥 넘김
        cur_child = sorted(cur) # 아직이면 자식 노드를 정렬하고

        for kid in cur_child:     # 하나씩 받음
            print("--"*lvl + kid) # 받은 자식을 출력
            self.tree(lvl+1, cur[kid]) # 아직 남아있을 수 있으니 더 깊이 탐색


n = int(input())
trie = Trie()      # 트라이
for _ in range(n):
    k, *l = input().split()
    trie.insert(l) # 추가

trie.tree(0, trie.r00t)