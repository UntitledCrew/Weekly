import sys


input = lambda : sys.stdin.readline().rstrip()

def solution():
    def find(n):
        print(parent)
        if parent[n] == 'N':
            parent[n] = -(n - 1)
            return n

        if parent[n] == 0:
            return 'end'

        parent[n] = find(parent[n])
        return parent[n]

    def union(n):
        if type(parent[n]) == int and parent[n] < 0:
            parent[-parent[n]] = n



    G = int(input())
    P = int(input())

    parent = ['N'] * (G + 1)

    is_finish = False
    answer = 0
    for p in range(1, P + 1):
        num = int(input())
        if is_finish:
            continue
        if find(num) == 'end':
            is_finish = True
            answer = p - 1
    if not is_finish:
        answer = p
    return answer


print(solution())
