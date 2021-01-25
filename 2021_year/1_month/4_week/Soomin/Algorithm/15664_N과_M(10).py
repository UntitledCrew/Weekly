import sys

input = lambda : sys.stdin.readline().strip()

def recur(idx, cnt):
    global N, M
    if cnt > M:
        print(' '.join(map(str, answer_list)))
        return
    last_num = False
    for i in range(idx, N):
        num = num_list[i]
        if last_num and num == last_num:
            continue
        if not visited[i]:
            visited[i] = True
            answer_list.append(num)
            recur(i + 1, cnt + 1)
            visited[i] = False
            last_num = answer_list.pop()

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = []

visited = [False] * N

recur(0, 1)
