from sys import stdin
input = lambda:stdin.readline().strip()

import heapq

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.chain = 0

    def leftCheck(self):
        if self.left:return self.left.chain
        else: return 0

    def rightCheck(self):
        if self.right:return self.right.chain
        else: return 0

    
    def chainCheck(self):
        cond = self.leftCheck()+1+self.rightCheck()
        if cond<=k:return cond
        else: return 0


n, k = map(int, input().split())
cows = []
for num in range(n):
    eff = int(input())
    heapq.heappush(cows, (-eff, num+1))

linkedlist = [Node()for _ in range(n+1)]
for num in range(1, n):
    linkedlist[num].right = linkedlist[num+1]
    linkedlist[num+1].left = linkedlist[num]

result = 0
for _ in range(n):
    eff, num = heapq.heappop(cows)

    now = linkedlist[num]
    # continuous cows count
    ccc = now.chainCheck()
    now.chain = ccc

    if not ccc:continue
    else:result -= eff

    if now.leftCheck():
        now.left.right = now.right
        now.left.chain = ccc

    if now.rightCheck():
        now.right.left = now.left
        now.right.chain = ccc

print(result)



'''
힌트 1. 소들끼리는 서로의 정보를 알고 있다
힌트 2. 덱을 사용한다

추론
1. 연결 리스트로 덱을 구현
2. 우선순위 큐를 이용해서 극한의 효율을 자랑하는 소를 순서대로 가져옴
3. 소에게 연속된 항목에 포함되는지 유효성 검사
4. 효율성으로 먼저 받고 연속 항목 어디에 포함되는지 확인


'''