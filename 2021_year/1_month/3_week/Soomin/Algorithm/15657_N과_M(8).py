import sys

input = lambda : sys.stdin.readline().strip()

def recur(idx, m):
    global N
    if not m:
        print(' '.join(map(str, answer_list)))
        return
    for i in range(idx, N):
        answer_list.append(num_list[i])
        recur(i, m - 1)
        answer_list.pop()

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = []

recur(0, M)
