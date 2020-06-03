import sys,bisect;input=sys.stdin.readline
from collections import deque
for i in range(int(input())):
    d=deque()
    dic={}
    for j in range(int(input())):
        cmd=input().split()
        cmd[1]=int(cmd[1])
        if cmd[0] == 'I':
            try:
                dic[cmd[1]]+=1
            except:
                dic[cmd[1]]=1
                bisect.insort_left(d,cmd[1])
        elif dic:
            if cmd[1]==-1:
                if dic[d[0]]==1:
                    del dic[d.popleft()]
                else:
                    dic[d[0]]-=1
            else:
                if dic[d[-1]]==1:
                    del dic[d.pop()]
                else:
                    dic[d[-1]]-=1
    if d:
        print(d[-1],d[0])
    else:
        print("EMPTY")