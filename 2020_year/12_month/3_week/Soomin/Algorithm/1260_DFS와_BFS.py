from collections import deque

def DFS(start):
    global N
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        if not dfs_visited[node]:
            dfs_visited[node] = 1
            dfs_answer.append(node)
            if len(dfs_answer) == N:
                break
            for tmp_node in D[node]:
                if not dfs_visited[tmp_node]:
                    stack.append(tmp_node)

def BFS(start):
    que = deque()
    que.append(start)
    while que:
        node = que.popleft()
        if not bfs_visited[node]:
            bfs_visited[node] = 1
            bfs_answer.append(node)
            for tmp_node in D[node]:
                if not bfs_visited[tmp_node]:
                    que.append(tmp_node)


N, M, V = map(int, input().split())

D = {n:[] for n in range(1, N + 1)}
dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)
dfs_answer = []
bfs_answer = []

for m in range(M):
    node1, node2 = map(int, input().split())
    D[node1].append(node2)
    D[node2].append(node1)

for key in D.keys():
    D[key].sort(reverse=True)

DFS(V)

for key in D.keys():
    D[key].sort()

BFS(V)

print(' '.join(map(str, dfs_answer)))
print(' '.join(map(str, bfs_answer)))