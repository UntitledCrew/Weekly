import sys

input = lambda : sys.stdin.readline().strip()

def recur(m):
    global N
    if not m:
        print(' '.join(map(str, num_list)))
        return
    for i in range(1, N + 1):
        num_list.append(i)
        recur(m - 1)
        num_list.pop()



N, M = map(int, input().split())
num_list = []

recur(M)
