import sys
sys.stdin = open('./dev/stdin')

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

print(data)