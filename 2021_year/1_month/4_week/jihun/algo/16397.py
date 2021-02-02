import sys
sys.stdin = open('./dev/stdin')

from collections import deque

def bfs(s, t, g):
    queue = deque()
    queue.append(s)
    checked[s] = 1
    while queue:
        q = queue.popleft()
        cnt = checked[q]
        if (q == g):
            return cnt - 1
        if (cnt > t):
            return 'ANG'
        if (0 <= q < 100000):
            if (q+1 < 100000):
                if (not checked[q+1]):
                    queue.append(q+1)
                    checked[q+1] = cnt + 1
            if (q*2 < 100000):
                q_2 = '{}'.format(q*2)
                b_btn = int('{}'.format(int(q_2[0:1])-1) + q_2[1:])
                if (not checked[b_btn] and b_btn != 0):
                    queue.append(b_btn)
                    checked[b_btn] = cnt + 1
    return 'ANG'
            

N, T, G = list(map(int, input().split()))

checked = [0] * 100000

print(bfs(N, T, G))