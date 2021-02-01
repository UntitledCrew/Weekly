import sys


input = lambda : sys.stdin.readline().rstrip()

def solution():
    def find(f):
        if type(parent[f]) == int:
            return f

        parent[f] = find(parent[f])
        return parent[f]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a == parent_b:
            return how_many[parent_a]

        if parent[parent_a] > parent[parent_b]:
            parent[parent_b] = parent_a
            how_many[parent_a] += how_many[parent_b]
            return how_many[parent_a]
        elif parent[parent_a] < parent[parent_b]:
            parent[parent_a] = parent_b
            how_many[parent_b] += how_many[parent_a]
            return how_many[parent_b]
        else:
            parent[parent_a] += 1
            parent[parent_b] = parent_a
            how_many[parent_a] += how_many[parent_b]
            return how_many[parent_a]

    F = int(input())
    parent = {}
    how_many = {}
    answer = []

    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = 1
            how_many[f1] = 1
        if f2 not in parent:
            parent[f2] = 1
            how_many[f2] = 1
        answer.append(union(f1, f2))

    return '\n'.join(map(str, answer))


T = int(input())

for tc in range(T):
    print(solution())