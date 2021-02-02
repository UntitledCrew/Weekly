import sys


input = lambda : sys.stdin.readline().rstrip()

def solution():
    def find(n):
        if parent[n] < 0:
            return n

        parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a == parent_b:
            return
        parent[parent_b] = parent_a

    N = int(input())
    M = int(input())

    cities = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(lambda x: int(x) - 1, input().split()))

    parent = [-1] * N

    for i in range(N):
        for j in range(i + 1, N):
            if cities[i][j]:
                union(i, j)

    root = find(plan[0])
    for idx in range(1, M):
        if root != find(plan[idx]):
            return 'NO'
    return 'YES'

print(solution())