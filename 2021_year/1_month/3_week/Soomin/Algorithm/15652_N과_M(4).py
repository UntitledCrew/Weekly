import sys

input = lambda : sys.stdin.readline().strip()

def recur(num, m):
    global N
    if not m:
        print(' '.join(map(str, num_list)))
        return
    for i in range(num, N + 1):
        num_list.append(i)
        recur(i, m - 1)
        num_list.pop()

N, M = map(int, input().split())
num_list = []

recur(1, M)
