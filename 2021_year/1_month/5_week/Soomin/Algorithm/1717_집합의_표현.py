import sys


input = lambda : sys.stdin.readline().rstrip()

def solution():
    def find(num):
        if parent[num] < 0:
            return num

        parent[num] = find(parent[num])
        return parent[num]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        if parent_a == parent_b:
            return

        if parent[parent_a] < parent[parent_b]:

            parent[parent_b] = parent_a
        elif parent[parent_a] > parent[parent_b]:
            parent[parent_a] = parent_b
        else:
            parent[parent_a] -= 1
            parent[parent_b] = parent_a

    n, m = map(int, input().split())
    parent = [-1] * (n + 1)

    answer = []

    for _ in range(m):
        command, a, b = map(int, input().split())
        if command:
            if find(a) == find(b):
                answer.append('YES')
            else:
                answer.append('NO')
        else:
            union(a, b)

    return '\n'.join(answer)


print(solution())