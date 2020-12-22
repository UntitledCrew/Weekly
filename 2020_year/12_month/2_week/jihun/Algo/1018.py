import sys
sys.stdin = open('./dev/stdin')

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

startW = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]
startB = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]

answer = 98765321
for y in range(N):
    if y+8 <= N:
        for x in range(M):
            if x+8 <= M:
                tempB = 0
                tempW = 0
                for yy in range(8):
                    for xx in range(8):
                        if not (yy % 2):
                            if (data[y+yy][x+xx] != startB[yy][xx]):
                                tempB += 1
                            if (data[y+yy][x+xx] != startW[yy][xx]):
                                tempW += 1
                        else:
                            if (data[y+yy][x+xx] != startW[yy][xx]):
                                tempB += 1
                            if (data[y+yy][x+xx] != startB[yy][xx]):
                                tempW += 1
                temp = tempW if tempB > tempW else tempB
                if answer > temp:
                    answer = temp
print(answer)