from sys import stdin
input=lambda:stdin.readline().rstrip()



class Node:
    def __init__(self, flag=False) -> None:
        self.flag = flag
        self.child = {}

class Trie:
    def __init__(self) -> None:
        self.parents = Node()

    def insert(self, string): # 추가할 요소
        cur = self.parents    # 최상위 노드를 기준으로

        for char in string:              # 문자를 하나씩 받아옴
            if char not in cur.child:    # 이미 있는게 아니라면
                cur.child[char] = Node() # 추가
            cur = cur.child[char]        # 자식노드를 부모노드로 올림
        cur.flag = True                  # 말단노드에 단어의 끝임을 기록

    def search(self, pre): # 시간을 확인할 단어
        cur = self.parents # 최상위 노드에서 찾기 시작
        words = 0          # 시간

        for p in pre:          # 단어를 하나씩 찾을 예정
            cur = cur.child[p] # 첫번째 단어에서 시작
            if len(cur.child)>1 or cur.flag:words+=1 # 갈림길이 있다면 내가 직접 입력해야하니 +1
        return words                                 # 단어의 완성단계라면 끝났음을 알려야하기 때문에 +1, 더 있을 수 있으니 +1



while 1:
    try:
        n = int(input())
        trie = Trie()
        words = [input()for _ in range(n)]
        for w in words:trie.insert(w)    # 요소 추가

        s = 0
        for w in words:s+=trie.search(w) # 자동완성을 위해 필요한 시간
        print(f"{s/n:.2f}")
    except:break