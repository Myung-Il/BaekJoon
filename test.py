from collections import deque

def boyer_moore_search_all(pattern, text):
    """패턴을 text에서 모두 찾아서 인덱스 리스트로 반환"""
    M, N = len(pattern), len(text)
    if M > N:
        return []
    
    # bad character heuristic 만들기
    bad_char = {}
    for i in range(M-1):
        bad_char[pattern[i]] = M - 1 - i

    indices = []
    i = 0
    while i <= N - M:
        j = M - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            indices.append(i)
            i += 1  # 패턴 겹칠 수 있으니 한 칸씩 이동
        else:
            shift = bad_char.get(text[i+M-1], M)
            i += max(shift, 1)
    return indices

def check_pattern_at(text, idx):
    """링크드 리스트에서 idx, idx+1, idx+2 위치 문자열 3글자가 'PPC' or 'CPP'인지 검사"""
    # idx, idx+1, idx+2가 연결되어 있어야 함
    if idx is None:
        return False
    second = nxt[idx]
    if second is None:
        return False
    third = nxt[second]
    if third is None:
        return False

    triple = text[idx] + text[second] + text[third]
    return triple == "PPC" or triple == "CPP"

def add_if_pattern(idx, q, visited_patterns, text):
    if check_pattern_at(text, idx) and idx not in visited_patterns:
        q.append(idx)
        visited_patterns.add(idx)

# 입력
n = int(input())
s = input()

if n % 3 != 0:
    print("NO")
    exit()

# 링크드 리스트 형태로 문자열 저장 (배열로 인덱스 관리)
prev = [i - 1 for i in range(n)]
nxt = [i + 1 for i in range(n)]
prev[0] = None
nxt[-1] = None

alive = [True]*n  # 제거 여부 표시

# 초기 패턴 위치 찾기: 두 패턴 모두 찾아서 합침
pattern1 = "PPC"
pattern2 = "CPP"
positions = []

positions += boyer_moore_search_all(pattern1, s)
positions += boyer_moore_search_all(pattern2, s)

# 중복 제거 및 정렬
positions = sorted(set(positions))

q = deque()
visited_patterns = set()

for pos in positions:
    q.append(pos)
    visited_patterns.add(pos)

# 제거 진행
while q:
    idx = q.popleft()
    # idx 위치가 아직 살아있는지, 그리고 idx+1, idx+2도 살아있는지 확인
    if idx is None or not alive[idx]:
        continue
    second = nxt[idx]
    if second is None or not alive[second]:
        continue
    third = nxt[second]
    if third is None or not alive[third]:
        continue

    triple = s[idx] + s[second] + s[third]
    if triple != "PPC" and triple != "CPP":
        continue

    # 제거: idx, second, third 제거 표시
    alive[idx] = False
    alive[second] = False
    alive[third] = False

    # 링크드 리스트 연결 갱신
    left = prev[idx]
    right = nxt[third]

    if left is not None:
        nxt[left] = right
    if right is not None:
        prev[right] = left

    # 제거한 위치 주변 새로 생긴 3글자 구간 검사 → 최대 2군데만 체크
    # 왼쪽 시작 위치 candidate
    check_pos = []
    if left is not None:
        check_pos.append(left)
        # 그 앞 위치도 체크
        if prev[left] is not None:
            check_pos.append(prev[left])
    # 오른쪽 시작 위치 candidate
    if right is not None:
        check_pos.append(right)
    
    for cpos in check_pos:
        if cpos is not None and alive[cpos]:
            # 새로운 패턴 발견 시 큐에 추가
            if check_pattern_at(s, cpos) and cpos not in visited_patterns:
                q.append(cpos)
                visited_patterns.add(cpos)

# 결과 확인
if all(not x for x in alive):
    print("YES")
else:
    print("NO")
