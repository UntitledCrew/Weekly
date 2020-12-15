import sys
sys.stdin = open('./dev/stdin')

data = int(input())

def recursive(current, depth):
    for i in range(10):
        if (depth != 0):
            target_num = '{}{}'.format(current, i)
        else:
            target_num = '{}'.format(i)
        
        target_sum = 0
        for part in target_num:
            target_sum += int(part)
        
        if (int(target_num) + target_sum == data):
            return int(target_num)
        elif (int(target_num) > data):
            return 0
    return recursive(current+1, depth+1)


print(recursive(0,0))