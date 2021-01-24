import sys

input = lambda : sys.stdin.readline().strip()

def recur(num, m):
    global N
    if not m:
        print(' '.join(map(str, num_list)))
        return
    for n in range(num, N - m + 2):
        num_list.append(n)
        recur(n + 1, m - 1)
        num_list.pop()

N, M = map(int, input().split())
num_list = []

recur(1, M)
