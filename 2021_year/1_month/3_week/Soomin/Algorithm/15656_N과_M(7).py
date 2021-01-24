import sys

input = lambda : sys.stdin.readline().strip()

def recur(m):
    global N
    if not m:
        print(' '.join(map(str, answer_list)))
        return
    for i in num_list:
        answer_list.append(i)
        recur(m - 1)
        answer_list.pop()



N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = []

recur(M)
