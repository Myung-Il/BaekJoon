import sys   # 빠른 입력
import heapq # deque는 느림

# 입력, 라인으로 받기
input = sys.stdin.readline

# 전체 카드 수, n
# 사용한 카드 수, k
# 제약 조건의 수, p
n, k, p = map(int, input().split())

gph_1 = [[] for _ in range(k)] # 최대값 그래프
gph_2 = [[] for _ in range(k)] # 최소값 그래프
d_1 = [0] * k # 최대용 진입차수
d_2 = [0] * k # 최소용 진입차수
val = [0] * k # 각 위치의 카드값 (초기값은 나중에 설정)

for _ in range(p): # 위상 정렬
    a, b = map(int, input().split()) # Ca > Cb
    gph_1[b].append(a) # 역방향 = 최대를 구함
    gph_2[a].append(b) # 순방향 = 최소를 구함
    # 왜 그러는지는 이해가 안됨
    # 위상정렬은 더러운게 맞아

    d_1[a] += 1
    d_2[b] += 1

# 최대값 위상정렬
pq = [i for i in range(k) if d_1[i] == 0]
heapq.heapify(pq)

cur = n - k - 1
while pq:
    t = heapq.heappop(pq)
    val[t] = cur + 1
    cur += 1
    for nxt in gph_1[t]:
        d_1[nxt] -= 1
        if d_1[nxt] == 0:
            heapq.heappush(pq, nxt)

# 최소값 위상정렬
pq = [i for i in range(k) if d_2[i] == 0]
heapq.heapify(pq)

cur = k
while pq:
    t = heapq.heappop(pq)
    cur -= 1
    val[t] -= cur
    for nxt in gph_2[t]:
        d_2[nxt] -= 1
        if d_2[nxt] == 0:
            heapq.heappush(pq, nxt)

# 거듭제곱 함수
def fast_pow(base, power, mod):
    res = 1
    base %= mod
    while power:
        if power & 1:
            res = res * base % mod
        base = base * base % mod
        power >>= 1
    return res

# 최종 결과 계산
MOD = 10**9 + 7
res = 0
pow_n = [1] * (k)
for i in range(1, k):
    pow_n[i] = pow_n[i-1] * n % MOD

for i in range(k):
    res = (res + val[i] * pow_n[i]) % MOD

print(res)
