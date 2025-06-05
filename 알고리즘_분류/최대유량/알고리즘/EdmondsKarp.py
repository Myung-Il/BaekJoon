# This class represents a directed graph ( 이 클래스는 방향 그래프를 나타냅니다 )
# using adjacency matrix representation  ( 인접 행렬 표현 사용 )
from collections import deque

class Graph:
    def __init__(self, graph):
        self.graph = graph # residual graph, ( 잔여 그래프 )
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    # 만약 잔여 그래프 안에 소스 s에서 싱크 t를 향하는 경로가 있다면 참값을 반환한다
    # 또한 경로를 저장하기 위해서 부모 리스트에 채운다

    def BFS(self, s, t, parent):
        # Mark all the vertices as not visited ( 모든 정점을 방문하지 않은 것으로 표시  )
        visited = [False]*(self.ROW)
        # Create a queue for BFS ( BFS를 위한 큐 생성 )
        queue = deque()

        # Mark the source node as visited and enqueue it ( 소스 노드를 방문한 것으로 표시 and 큐에 추가 )
        visited[s] = True
        queue.append(s)

        # Standard BFS Loop ( BFS 실행 )
        while queue:

            # Dequeue a vertex from queue and print it ( 큐에서 정점을 꺼냄 and 출력 )
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u ( 꺼낸 정점 u의 인접 정점들 모두 얻는다 )
            # If a adjacent has not been visited, then mark it ( 만약 방문 하지 않은 인접은 표시합니다 )
            # visited and enqueue it ( 방문 처리 후 큐에 넣습니다 )
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node, ( 만약 우리가 싱크 노드까지 찾았다면, )
                    # then there is no point in BFS anymore ( 그러면 더 이상 BFS 안에 대상은 없습니다 )
                    # We just have to set its parent and can return true ( 그저 부모를 설정하고 True를 반환하면 된다 )
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # We didn't reach sink in BFS starting from source, ( BFS 처음부터 싱크를 찾지 못함 )
        # so return false ( False를 반환한다 )
        return False
            
    
    # Returns the maximum flow from s to t in the given graph ( 주어진 그래프 s에서 t까지의 최대 유량을 반환 )
    def EdmondsKarp(self, source, sink):

        # This array is filled by BFS and to store path ( 이 배열은 BFS로 채워지고 경로를 저장한다 )
        parent = [-1]*(self.ROW)

        max_flow = 0 # There is no flow initially ( 처음에는 유량이 없다 )

        # Augment the flow while there is path from source to sink ( 소스에서 싱크로 경로로 가는 동안 유량은 증가한다 )
        while self.BFS(source, sink, parent) :

            # Find minimum residual capacity of the edges along the ( BFS로 채워진 경로를 따라 가장자리의 최소 잔여 용량 찾는다 )
            # path filled by BFS. Or we can say find the maximum flow ( 또는 찾은 경로를 통해 최소 유량을 찾을 수 있다 )
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow ( 전체 유량에 경로 유량 추가 )
            max_flow += path_flow

            # update residual capacities of the edges and ( 경로를 따라 가장자리와 반대편의 잔여 용량 업데이트 )
            # reverse edges along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Create a graph given in the above diagram ( 위 다이아그램에서 주어진 그래프 생성 ) ( 다이어 그램 없음 )
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0
sink = 5

print ("The maximum possible flow is %d " % g.EdmondsKarp(source, sink))