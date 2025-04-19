import sys
import heapq

input = sys.stdin.readline

n, k, p = map(int, input().split())

gph_1 = [[] for _ in range(k)]
gph_2 = [[] for _ in range(k)]
d_1 = [0] * k
d_2 = [0] * k
val = [0] * k

for _ in range(p):
    a, b = map(int, input().split())
    gph_1[b].append(a)
    gph_2[a].append(b)
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
