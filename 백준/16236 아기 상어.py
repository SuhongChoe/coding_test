import sys;input = sys.stdin.readline
from functools import cmp_to_key
N = int(input())

fishe = { i : list() for i in range(1,7)}
time = 0
shark = None
shark_eat_count = 0
shark_size = 2


for i in range(N):
    for j, cow in enumerate(list(map(int, sys.stdin.readline().split()))):
        if 1<= cow <=6:
            fishe[cow].append((i,j))
        elif cow == 9:
            shark = (i,j)

def cmp(x, y):
    if abs(shark[0]-x[0])+abs(shark[1]-x[1]) == abs(shark[0]-y[0])+abs(shark[1]-y[1]):
        if x[0] == y[0]:
            return x[1] < y[1]
        return x[0] < y[0]
    return abs(shark[0]-x[0])+abs(shark[1]-x[1]) < abs(shark[0]-y[0])+abs(shark[1]-y[1])

eat_fishe_list = fishe[1]
#,reverse=True
while(eat_fishe_list):
    print(f"before : {eat_fishe_list}")
    eat_fishe_list = sorted(eat_fishe_list, key=cmp_to_key(cmp))
    print(f"after : {eat_fishe_list}")
    eat_fishe = eat_fishe_list.pop()
    print(f"eat_fishe : {eat_fishe}")
    print(f"eat_fishe_list : {eat_fishe_list}")
    print(f"befor shark : {shark}")
    time += abs(shark[0]-eat_fishe[0]) + abs(shark[1]-eat_fishe[1])
    print(f"time : {time}")
    shark = eat_fishe
    print(f"befor shark : {shark}\n")
    shark_eat_count += 1
    if shark_size == shark_eat_count:
        shark_eat_count = 0
        shark_size += 1
        try:
            eat_fishe_list += fishe[shark_size-1]
        except:
            continue

print(time)


