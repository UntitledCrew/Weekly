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


N = int(input())
M = int(input())

D = {n:[] for n in range(1, N + 1)}
dfs_visited = [0] * (N + 1)
dfs_answer = []

for m in range(M):
    node1, node2 = map(int, input().split())
    D[node1].append(node2)
    D[node2].append(node1)

DFS(1)

print(len(dfs_answer)-1)