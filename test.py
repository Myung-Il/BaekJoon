import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

p = list(map(int, input().split()))
v = [0 for _ in range(8)]
pmt, res = [], []

def dfs(idx):
	if idx == 8:
		pmt.append(res[:])
		return
	for next in range(8):
		if v[next] == 0:
			v[next] = 1
			res.append(p[next])
			dfs(idx+1)
			res.pop()
			v[next] = 0

def ccw(a, b, c):
	x1, y1 = 0, a
	x2, y2 = ((b**2)/2)**0.5, ((b**2)/2)**0.5
	x3, y3 = c, 0
	l = (x1*y2+x2*y3+x3*y1)
	r = (x2*y1+x3*y2+x1*y3)
	temp = l-r
	if temp <= 0:
		return True
	return False
		
def checker(pmt):
	cnt = 0
	for idx in range(len(pmt)):
		flag = True
		for i in range(8):
			if not ccw(pmt[idx][i], pmt[idx][(i+1)%8], pmt[idx][(i+2)%8]):
				flag = False
				break
		if flag:
			cnt += 1
	return cnt


dfs(0)
print(checker(pmt))