import sys
from collections import deque

# 빠른 입출력 설정
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    try:
        line1 = input().split()
        if not line1: return
        N, M, C, D = map(int, line1)
        
        line2 = input().split()
        if not line2: return
        b = list(map(int, line2))
    except ValueError:
        return

    # DP 테이블 초기화: N행, M+1열
    dp = [[0] * (M + 1) for _ in range(N)]

    # 초기화 (i=0)
    for k in range(1, M + 1):
        dp[0][k] = M - abs(b[0] - k)

    # 메인 DP 루프
    for i in range(1, N):
        # C개의 나머지 그룹별로 처리 (j = 1 ~ C)
        for j in range(1, C + 1):
            dq = deque() # (dp_value, index) 저장
            
            # C++ 코드의 k 변수를 추적하기 위한 변수
            # 파이썬 for문은 루프가 끝나면 변수가 사라지거나 마지막 값만 남으므로 별도 관리
            current_k = j
            
            # [Phase 1] 덱에 값을 넣으면서 동시에 'target = k - aC' 위치의 DP 계산
            # k는 j부터 C씩 증가하며 M까지
            for k in range(j, M + 1, C):
                current_k = k # 루프 진행 상황 추적
                
                # 1. Pop Front (윈도우 관리)
                # 우리가 계산하려는 타겟(target)은 k - a*C 입니다.
                # 덱의 맨 앞(index)이 (target - a*C) 보다 작으면 제거해야 합니다.
                # 즉, index < k - 2*a*C
                limit_idx = k - 2 * D
                while dq and dq[0][1] < limit_idx:
                    dq.popleft()
                    
                # 2. Pop Back (단조성 유지)
                # 현재 dp[i-1][k] 값보다 작거나 같은 덱의 뒤쪽 요소 제거
                val = dp[i-1][k]
                while dq and dq[-1][0] <= val:
                    dq.pop()
                    
                # 3. Push (현재 값 덱에 추가)
                dq.append((val, k))
                
                # 4. DP 계산 (Target 위치)
                # 덱에는 현재 k(미래)까지의 값이 들어있음.
                # 계산할 위치는 k에서 D(=a*C)만큼 뒤인 곳.
                target = k - D
                if target > 0:
                    # 덱의 맨 앞이 최댓값
                    dp[i][target] = dq[0][0] + M - abs(b[i] - target)

                for y in dp:print(y)
                print(dq)
                    
            # [Phase 2] 남은 뒷부분 처리
            # C++ 로직상 for문이 끝나면 k는 M보다 큰 첫 번째 값이 됨 (current_k + C)
            # 따라서 Phase 2의 시작점 t는 (current_k + C) - a*C 부터 시작
            
            start_t = (current_k + C) - D
            
            for t in range(start_t, M + 1, C):
                if t > 0:
                    # Pop Front: 일반적인 윈도우 체크 (index < t - D)
                    # t - a*C == t - D
                    limit_idx = t - D
                    while dq and dq[0][1] < limit_idx:
                        dq.popleft()
                        
                    if dq:
                        dp[i][t] = dq[0][0] + M - abs(b[i] - t)

    # 정답 찾기 (마지막 행의 최댓값)
    ans = 0
    for k in range(1, M + 1):
        if dp[N - 1][k] > ans:
            ans = dp[N - 1][k]
            
    print(ans)

if __name__ == "__main__":
    solve()