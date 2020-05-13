import sys,bisect;input=sys.stdin.readline
from collections import deque
for i in range(int(input())):
    d=deque()
    dic={}
    for j in range(int(input())):
        cmd=input().split()
        cmd[1]=int(cmd[1])
        if cmd[0] == 'I':
            if cmd[1] in dic:
                dic[cmd[1]]+=1
            else:
                dic[cmd[1]]=1
                bisect.insort_left(d,cmd[1])
        elif dic:
            if cmd[1]==-1:

            else:
                heappop(heap_max)
                heap_min.pop()
    if heap_max:
        print(heappop(heap_max)[1],heappop(heap_min))
    else:
        print("EMPTY")