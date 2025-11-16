from sys import stdin
input = lambda:stdin.readline().strip()

from collections import deque

n, k = map(int, input().split())
psum = [0]
dp = []
for num in range(n):
    eff = int(input())
    psum.append(eff+psum[-1])

for i in range(k+1):dp.append(psum[i])
for i in range(k+1, n+1):
    c1 = dp[i-1]
    c2 = psum[i]+max([dp[j-1]-psum[j]for j in range(i-k, i)])
    dp.append(max(c1, c2))

print(dp[-1])


...
'''
[ 동적 계획법 ]

- 정의
1. psum : 누적합
2. dp : k개의 비연속 누적합

- 점화식 (1 <= flag <= k)
1. 현재 소를 선택하지 않았을 때 : dp[i-1]
2. 선택 했을 때 : max(psum[i]-psum[i-flag] + dp[i-flag-1]) : psum[i] + max(dp[j-1]-psum[j])
    - psum[i]-psum[i] : 특정 구간의 최대합
    - dp[i-flag-1] : 특정 구간 이전의 최대합
    - : i-flag = j
        >>> (1 <= i-j <= k) : (i-k <= j <= i-1) : 쉽게 보기
        >>> max(psum[i]-psum[j] + dp[j-1]) : psum[i] + max(dp[j-1]-psum[j])
3. 두 경우를 한꺼번에 볼 때 (단, (i-k <= j <= i)) : psum[i] + max(dp[j-1]-psum[j])

- 덱 이용 (슬라이딩 윈도우)
1. 지나간 위치는 dp에 저장이 되어 있음

'''