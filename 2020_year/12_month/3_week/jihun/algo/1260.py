import sys
sys.stdin = open("./dev/stdin")

N, M, V = list(map(int, input().split()))

flag = [1] + [0] * (N)
edge = [[0] * (N + 1) for _ in range(N+1)]

for i in range(M):
    s, g = list(map(int, input().split()))
    edge[s][g] = 1
    edge[g][s] = 1

dfs_answer = []
def dfs(n, v):
    if (0 not in flag):
        return
    if (flag[v] == 0):
        flag[v] = 1
        dfs_answer.append(v)
    else:
        return
    for i in range(1, n+1):
        if edge[v][i] == 1 and flag[i] == 0:
            dfs(n, i)
dfs(N, V)

flag = [1] + [0] * (N)
check = [[0] * (N + 1) for _ in range(N+1)]

bfs_answer = []
queue = []
def bfs(n, v):
    queue = [v]
    while queue:
        stack = queue.pop(0)
        flag[stack] = 1
        bfs_answer.append(stack)
        if (0 not in flag):
            return
        for i in range(1, n+1):
            if (edge[stack][i] and not flag[i]):
                queue.append(i)

bfs(N, V)

print(*dfs_answer)
print(*bfs_answer)