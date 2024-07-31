from sys import stdin
input = lambda:stdin.readline().rstrip()

def bt(e):
    left, right = 0, len(dp)
    while left<right:           # 이분탐색을 이용해서
        mid = (left+right)//2   # e가 갈 수 있는 가장 작은 수쪽으로 보낸다
        if dp[mid]<e:left=mid+1 # ex) 10 7 6 3, e = 5
        else:right=mid          # ex) 10 7 6 5 로 정정
    return right                # 정정될 위치를 반환

n = int(input())
a = list(map(int,input().split()))

dp, idxn = [-float("inf")], [0]*n # NlogN을 위해서 
for idx in range(n):      # 처음부터 끝까지 N개를 검사
    if dp[-1]<a[idx]:     # 지금 조사한게 이전것보다 크다면 
        point = len(dp)   # 길이를 늘리고
        dp.append(a[idx]) # 저장
    else:
        point = bt(a[idx]) # 작거나 같다면 bt로 이동
        dp[point] = a[idx] # 정정된 위치에 저장
    idxn[idx] = point      # 저장하고 있는 숫자가 이전 것에 비해서
                           # 몇번째로 얼마나 큰지 기록

result, mx = [], max(idxn)
for idx in range(n-1, -1, -1): # 역순으로
    if idxn[idx]==mx:          # 가장큰 자리번째부터 조사
        result.append(a[idx])  # 조사 한 것을 저장
        mx -= 1                # 다음 큰 자리로 변경

print(len(result))
print(*result[::-1])