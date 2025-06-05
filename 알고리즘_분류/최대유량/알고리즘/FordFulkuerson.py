# Ford-Fulkerson Method ( 포드 풀커슨 메소드 )
# This implementation can be inefficient for certain graphs ( 이 구현은 특정 그래프에 대해 비효율적일 수 있고 )
# and may not terminate if capacities are irrational numbers. ( 용량이 무리수인 경우 종료 되지 않을 수 있다 )

# Number of vertices ( 정점의 수 )
V = 6

# DFS to find an augmenting path ( 증가 경로 찾기 위한 DFS  )
def dfs(rGraph, s, t, parent, visited):
    visited[s] = True
    if s == t:
        return True

    for v in range(V):
        # rGraph[s][v] > 0 means there's remaining capacity ( rGraph[s][v] > 0은 남은 용량을 의미한다 )
        if rGraph[s][v] > 0 and not visited[v]:
            parent[v] = s # Store path ( 저장된 경로 )
            if dfs(rGraph, v, t, parent, visited):
                return True
    return False

# Returns the maximum flow from s to t in the given graph ( 주어진 그래프에서 s에서 t까지의 최대 유량을 반환 )
def ford_fulkerson_dfs(graph, s, t):
    # Create residual graph and fill with initial capacities ( 잔여 그래프를 생성하고 초기 용량을 채운다 )
    rGraph = [[0] * V for _ in range(V)]
    for u in range(V):
        for v in range(V):
            rGraph[u][v] = graph[u][v]

    parent = [-1] * V # Array to store path ( 경로를 저장할 배열 )
    max_flow = 0

    # Augment the flow while there is a path from source to sink ( 소스에서 싱크까지 경로 동안 유량은 증가한다 )
    # Note: visited array must be reset for each DFS call ( 참고: 방문한 배열은 각 DFS 호출마다 재설정해야 한다 )
    while True:
        visited = [False] * V
        if not dfs(rGraph, s, t, parent, visited):
            break # No more augmenting paths ( 더 이상 증가할 경로가 없다면 )

        # Find bottleneck capacity of the found path ( 찾았던 경로 중 꽉찬 용량을 찾는다 )
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, rGraph[u][v])
            v = parent[v]

        # Update residual capacities along the path
        v = t
        while v != s:
            u = parent[v]
            rGraph[u][v] -= path_flow # Forward edge capacity reduction
            rGraph[v][u] += path_flow # Backward edge capacity increase
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Driver program to test above functions ( 위의 기능을 테스트하는 드라이버 프로그램 )
if __name__ == "__main__":
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    source = 0
    sink = 5

    print("The maximum possible flow is", ford_fulkerson_dfs(graph, source, sink))