import sys
sys.stdin = open('./dev/stdin')


def dfs(s):
    global idx
    checked[s] = 1
    nums.append(s)
    ns = data[s]

    if (not checked[ns]):
        dfs(ns)
    else:
        if (ns in nums):
            idx = nums.index(ns)
        return

T = int(input())

for _ in range(T):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    checked = [0] * (N + 1)

    cnt = 0

    for i in range(1, len(data)):
        if not checked[i]:
            nums = []
            idx = -1
            dfs(i)
            if (idx != -1):
                cnt += len(nums[idx:])

    print(N - cnt)
