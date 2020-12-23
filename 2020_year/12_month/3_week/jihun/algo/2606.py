import sys
sys.stdin = open("./dev/stdin")

N = int(input())
M = int(input())
data = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, g = list(map(int, input().split()))
    data[s][g] = 1
    data[g][s] = 1
checked = [0] * (N + 1)

def bfs(n, s):
    queue = [s]
    checked[s] = 1
    while queue:
        stack = queue.pop(0)
        for i in range(1, n+1):
            if (data[stack][i] and not checked[i]):
                queue.append(i)
                checked[i] = 1

bfs(N, 1)
print(checked.count(1) - 1)