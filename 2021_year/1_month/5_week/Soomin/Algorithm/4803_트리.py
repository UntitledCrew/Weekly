import sys


input = lambda : sys.stdin.readline().rstrip()

def solution():
    def find(n):
        if parent[n] < 0:
            return n
        if parent[n] == 0:
            return 0
        parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a == parent_b:
            parent[parent_a] = 0
            return

        if not parent_a:
            parent[parent_b] = 0
            return

        if not parent_b:
            parent[parent_a] = 0
            return

        if parent[parent_a] < parent[parent_b]:
            parent[parent_b] = parent_a
        elif parent[parent_a] > parent[parent_b]:
            parent[parent_a] = parent_b
        else:
            parent[parent_a] -= 1
            parent[parent_b] = parent_a

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        return False
    parent = [0] + [-1] * n
    for e in range(m):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    answer = 0
    for p in parent:
        if p < 0:
            answer += 1

    if not answer:
        return 'No trees.'
    elif answer == 1:
        return 'There is one tree.'
    else:
        return 'A forest of {} trees.'.format(answer)


tc = 0
while True:
    answer = solution()

    if not answer:
        break

    tc += 1
    print('Case {}: {}'.format(tc, answer))