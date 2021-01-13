from collections import deque
import sys

def bfs(n):
    que = deque()
    que.append(n)
    visited[n] = 1
    while que:
        node = que.popleft()
        test_group = D[node]
        from_group_num = visited[node]
        for test_num in test_group:
            if visited[test_num]:
                if visited[test_num] == from_group_num:
                    return False
                else:
                    continue
            else:
                que.append(test_num)
                visited[test_num] = 3 - from_group_num
    for idx in range(1, len(visited)):
        if not visited[idx]:
            visited[idx] = 1
            if D[idx]:
                if not bfs(idx):
                    return False
    return True

input = sys.stdin.readline

K = int(input())

for tc in range(K):
    V, E = map(int, input().split())
    D = {v : [] for v in range(1, V+1)}
    visited = [0] * (V + 1)
    for e in range(E):
        n1, n2 = map(int, input().split())
        D[n1].append(n2)
        D[n2].append(n1)

    for i in range(1, V + 1):
        if D[i]:
            break

    result = bfs(i)
    if result:
        print('YES')
    else:
        print('NO')