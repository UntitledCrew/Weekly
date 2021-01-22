import sys

input = lambda : sys.stdin.readline().strip()

def recur(m):
    global N
    if not m:
        print(' '.join(map(str, num_list)))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            num_list.append(i)
            visited[i] = True
            recur(m - 1)
            num_list.pop()
            visited[i] = False



N, M = map(int, input().split())
num_list = []
visited = [False] * (N + 1)

recur(M)
