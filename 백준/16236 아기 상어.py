import sys;input = sys.stdin.readline
from functools import cmp_to_key
N = int(input())

fishe = { i : list() for i in range(1,7)}
time = 0
shark = None
shark_eat_count = 0
shark_size = 2

map = [ (i,j,size) for i in range(N) for j, size in enumerate(list(map(int, sys.stdin.readline().split()))) ]


for i in range(N):
    for j, cow in enumerate(list(map(int, sys.stdin.readline().split()))):
        if 1<= cow <=6:
            fishe[cow].append((i,j))
        elif cow == 9:
            shark = (i,j)

eat_fishe_list = fishe[1]
#,reverse=True
while(eat_fishe_list):
    #print(f"before : {eat_fishe_list}")
    eat_fishe_list = sorted(eat_fishe_list, key=lambda x : ((abs(shark[0]-x[0])+abs(shark[1]-x[1])), x[0], x[1]), reverse=True)
    #print(f"after : {eat_fishe_list}")
    eat_fishe = eat_fishe_list.pop()
    #print(f"eat_fishe : {eat_fishe}")
    #print(f"eat_fishe_list : {eat_fishe_list}")
    print(f"shark : {shark} => eat_fishe : {eat_fishe}")
    time += (abs(shark[0]-eat_fishe[0]) + abs(shark[1]-eat_fishe[1]))
    print(f"time : {time}")
    shark = eat_fishe
    #print(f"after shark : {shark}\n")
    shark_eat_count += 1
    print(shark_size, shark_eat_count)
    if shark_size == shark_eat_count:
        shark_eat_count = 0
        shark_size += 1
        try:
            eat_fishe_list += fishe[shark_size-1]
        except:
            continue

print(time)


