


def dfs(graph, v, visited):
    visited[v]= True

    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],         # 노드 0은 사용하지 않음
    [2, 3, 8],  # 1번 노드와 연결된 노드들
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)



