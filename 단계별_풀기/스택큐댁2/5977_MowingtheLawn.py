from sys import stdin
input = lambda:stdin.readline().strip()

from collections import deque

n, k = map(int, input().split())
psum = [0]
for num in range(n): psum.append(int(input())+psum[-1])

dp = [0]*(n+1)
swp = deque([0])

def calculation(j):
    if j==0:return 0
    else: return dp[j-1]-psum[j]

for i in range(1, n+1):
    # 슬라이딩 범위를 벗어난 요소를 제거
    while swp and swp[0] < i-k:swp.popleft()

    # 최대 연속 합 구하기
    dp[i] = max(dp[i-1], psum[i]+calculation(swp[0]))

    # 연속 구간에 대한 다른 경우 중 최적 찾기
    new = calculation(i)
    while swp and calculation(swp[-1]) <= new:swp.pop()

    swp.append(i)

print(dp[-1])


...
'''
[ 동적 계획법 ]

- 정의
1. psum : 누적합
2. dp : k개의 연속 누적합

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