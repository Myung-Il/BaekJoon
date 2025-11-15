from sys import stdin
input = lambda:stdin.readline().strip()

import heapq

n, k = map(int, input().split())
cows = []
for num in range(n):
    eff = int(input())
    heapq.heappush(cows, (-eff, num+1))


class Node:
    def __init__(self, l, r, n):
        self.left = l
        self.right = r
        self.chain = n
        

linkedlist = [None]*(n+2)
for num in range(1, n+1):
    linkedlist[num] = Node(linkedlist[num-1], linkedlist[num+1], 0)

res = 0
for _ in range(n):
    eff, num = heapq.heappop(cows)

    now = linkedlist[num]
    if not now.chain:
        chain = now.left.chain+1+now.right.chain
        if chain<k:
            now.chain = chain
            now.left.chain = chain
            now.right.chain = chain
            res -= eff

print(res)



'''
힌트 1. 소들끼리는 서로의 정보를 알고 있다
힌트 2. 덱을 사용한다

추론
1. 연결 리스트로 덱을 구현
2. 우선순위 큐를 이용해서 극한의 효율을 자랑하는 소를 순서대로 가져옴
3. 소에게 연속된 항목에 포함되는지 유효성 검사
4. 효율성으로 먼저 받고 연속 항목 어디에 포함되는지 확인

'''