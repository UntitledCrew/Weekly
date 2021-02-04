import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

def bfs(N):
    global T, G
    que = deque()
    que.append((N, 0))
    visited[N] = True
    if N == G:
        return 0
    while que:
        n, cnt = que.popleft()
        if cnt >= T:
            return "ANG"
        n1 = n + 1
        n2 = False
        if n * 2 < 100000:
            n2 = n * 2
            s2 = str(n2)
            for i in range(len(s2)):
                i2 = int(s2[i])
                if i2:
                    s2 = s2.replace(s2[i], str(i2 - 1), 1)
                    break
            n2 = int(s2)
        if n1 == G or n2 == G:
            return cnt + 1
        if n1 < 100000 and not visited[n1]:
            visited[n1] = True
            que.append((n1, cnt + 1))
        if n2 and not visited[n2]:
            visited[n2] = True
            que.append((n2, cnt + 1))
    return "ANG"

N, T, G = map(int, input().split())
visited = [False] * 100000

print(bfs(N))
