import sys, math
input = sys.stdin.readline

N = int(input().strip())

x = int(math.ceil(N**0.5))   # or int((N-1)**0.5)+1
K = 2 * x

print(K)
# 앞 x개는 1, 뒤 x개는 x
print(" ".join(["1"] * x + [str(x)] * x))
