import sys

input = lambda : sys.stdin.readline().strip()

def recur(cnt):
    global N, M
    if cnt > M:
        print(' '.join(map(str, answer_list)))
        return
    last_num = False
    for i in range(N):
        num = num_list[i]
        if last_num and num == last_num:
            continue
        answer_list.append(num)
        recur(cnt + 1)
        last_num = answer_list.pop()

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = []

recur(1)
