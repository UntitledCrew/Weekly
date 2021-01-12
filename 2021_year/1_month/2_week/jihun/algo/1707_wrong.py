import sys
sys.stdin = open('./dev/stdin')

from collections import deque

def bfs():
    queue = deque()
    queue.append([1])
    color = 1
    checked[1] = color
    while queue:
        color = 2 if color == 1 else 1
        q_list = queue.popleft()
        for q in q_list:
            temp = []
            for i in range(len(data[q])):
                if data[q][i]:
                    if (checked[q] == color):
                        return 'NO'
                    else:
                        checked[i] = color
                    temp.append(i)
            flag[q] = 1
            if (flag.count(0) == 1):
                return 'YES'
            queue.append(temp)


K = int(input())
for _ in range(K):
    V, E = list(map(int, input().split()))
    data = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, g = list(map(int, input().split()))
        data[s][g] = 1
        data[g][s] = 1
    checked = [0] * (V + 1)
    flag = [0] * (V + 1)
    print(bfs())

