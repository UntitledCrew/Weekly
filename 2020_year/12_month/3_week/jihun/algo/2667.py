import sys
sys.stdin = open("./dev/stdin")

N = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

data = []
for _ in range(N):
    data.append(list(map(int, list(input()))))

checked = [[0] * (N) for _ in range(N)]

def dfs(y, x, idx):
    checked[y][x] = idx
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if (0 <= yy < N and 0 <= xx < N and not checked[yy][xx] and data[yy][xx]):
            dfs(yy, xx, idx)

idx = 1
for y in range(N):
    for x in range(N):
        if (data[y][x] and not checked[y][x]):
            dfs(y, x, idx)
            idx += 1

print(idx-1)
answer = []
for i in range(idx-1):
    cnt = 0
    for row in checked:
        cnt += row.count(i+1)
    answer.append(cnt)
print('\n'.join(list(map(str, sorted(answer)))))