# 1. Source에서 SInk로 가는 경로를 하나 찾습니다.
def findPath():
    # dfs or bfs
    # c(a, b) - f(a, b) > 0 조건에 따라서 path을 찾을 수 있게 함.
    pass

def getMaxTotalFlow():
    total = 0
    path = 0
    while path is not None:  # 경로 찾기 및 반복
        # 2. 찾아낸 경로에 보낼수 있는 최대 flow을 찾습니다.
        path = findPath()
        f = None
        for p in path:
            path_flow = p.capacity - p.flow
            if f is None: f = path_flow
            else:         f = min(f, path_flow)

        # 3. 찾아낸 경로에 실제 flow을 흘려보냅니다.
        for p in path:
            # 순방향에는 + 로 흘려줍니다.
            path(p.a, p.b).flow += f
            # 역방향에는 - 로 흘려줍니다.
            path(p.b, p.a).flow -= f

        total += f

    # total 이 최대 유량이 됩니다.
    return total