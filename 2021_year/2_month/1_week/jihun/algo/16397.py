import sys
sys.stdin = open('./dev/stdin')

from collections import deque

def bfs(s, t, g):
    queue = deque()
    queue.append(s)
    checked[s] = 0
    while queue:
        q = queue.popleft()
        cnt = checked[q]
        if (cnt > t):
            break
        if (q == g):
            return cnt
        if (q+1 < 100000):
            if (not checked[q+1]):
                queue.append(q+1)
                checked[q+1] = cnt + 1
        if (q*2 < 100000 and q):
            q_2 = '{}'.format(q*2)
            b_btn = int('{}'.format(int(q_2[0:1])-1) + q_2[1:])
            if (not checked[b_btn]):
                queue.append(b_btn)
                checked[b_btn] = cnt + 1
    return 'ANG'
            

N, T, G = list(map(int, input().split()))

checked = [0] * 100001

print(bfs(N, T, G))


# from collections import deque

# def bfs():
#     q = deque()
#     q.append(n)
#     dist[n] = 0
#     while q:
#         x = q.popleft()
#         if dist[x] > t:
#             break
#         if x == g:
#             print(dist[x])
#             return
#         dx = [(x+1), (x*2)]
#         for i in range(2):
#             nx = dx[i]
#             if nx > 99999:
#                 continue
#             if i and x:
#                 nx -= 10**(len(str(nx))-1)
#             if dist[nx] == -1:
#                 q.append(nx)
#                 dist[nx] = dist[x]+1
#     print("ANG")

# n, t, g = map(int, input().split())
# dist = [-1]*100000
# bfs()