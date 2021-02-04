import sys

input = lambda : sys.stdin.readline().strip()

def dfs():
    global n
    answer = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        level = i
        cnt = 0
        while True:
            if visited[i] and level == visited[i][0]:
                break
            cnt += 1
            if visited[i]:
                visited[i] = (level, cnt)
                break
            visited[i] = (level, cnt)
            i = D[i]
        answer += visited[i][1] - 1
    return answer

T = int(input())
for tc in range(T):
    n = int(input())
    selected = list(map(int, input().split()))

    D = dict(zip([i for i in range(1, n+1)], selected))

    visited = [0] * (n + 1)

    print(dfs())