import math

# 구간 내 최댓값 갱신
def make_tree(left, right, node, idx, value):
    seg_tree[node] = max(seg_tree[node], value) 
    if left == right:
        return
    mid = (left+right) // 2 
    if idx <= mid:
        make_tree(left, mid, node*2, idx, value)
    else:
        make_tree(mid+1, right, node*2+1, idx, value)

# [start, end] 구간 내의 최댓값 반환
def find_max(left, right, node, start, end):
    if start > right or end < left:
        return -math.inf
    if left == right:
        return seg_tree[node]
    if start <= left and right <= end:
        return seg_tree[node]
    mid = (left+right) // 2 
    return max(find_max(left, mid, node*2, start, end), find_max(mid+1, right, node*2+1, start, end))
    
n, d = map(int, input().split())
# 인덱스를 1부터 사용하기 위함
dp = [0]
# 시작한 지점에서 바로 나가는 경우가 초기값
dp.extend(map(int, input().split()))
seg_tree = [-math.inf]*(n*4)
for i in range(1, n+1):
	# 최댓값 갱신
    dp[i] = max(dp[i], dp[i]+find_max(1, n, 1, i-d, i-1))
    # 만들어진 최댓값을 세그먼트 트리에 삽입
    make_tree(1, n, 1, i, dp[i])
print(max(dp[1:]))