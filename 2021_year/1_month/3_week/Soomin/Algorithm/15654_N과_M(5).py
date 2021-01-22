import sys

input = lambda : sys.stdin.readline().strip()

def recur(m):
    global N
    if not m:
        print(' '.join(map(str, answer_list)))
        return
    for i in num_list:
        if not visited[i]:
            answer_list.append(i)
            visited[i] = True
            recur(m - 1)
            answer_list.pop()
            visited[i] = False



N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = []
visited = [False] * (num_list[-1] + 1)

recur(M)
