import sys
sys.stdin = open('./dev/stdin')

from collections import deque

def bfs(n):
    queue = deque()
    queue.append([n])
    color = 1
    checked[n] = color
    while queue:
        color = 2 if color == 1 else 1
        q_list = queue.popleft()
        temp = []
        for q in q_list:
            for next_node in data[q]:
                if (checked[q] == color):
                    return 'NO'
                else:
                    checked[next_node] = color
                if (node[next_node]):
                    temp.append(next_node)
            node[q] = 0
            if (node.count(0) == V+1):
                return 'YES'
        queue.append(temp)


K = int(input())
for _ in range(K):
    V, E = list(map(int, input().split()))
    data = {}
    node = [0] * (V+1)
    for _ in range(E):
        s, g = list(map(int, input().split()))
        if (not data.get(s)):
            data[s] = set()
        if (not data.get(g)):
            data[g] = set()
        data[s].add(g)
        data[g].add(s)
        node[s] = 1
        node[g] = 1
    checked = [0] * (V + 1)

    for i in range(len(node)):
        if node[i]:
            print(bfs(i))
            break

