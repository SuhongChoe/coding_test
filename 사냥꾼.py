import sys;input=sys.stdin.readline
from bisect import *
n,m,l=map(int,input().split())
sade=sorted(list(map(int,input().split())))
cnt=0
for _ in range(m):
    x,y=map(int,input().split())
    a=bisect_left(sade, x)
    if(a>=n):
        a-=1
    if abs(sade[a]-x)+y<=l:
        cnt+=1
    elif abs(sade[a-1]-x)+y<=l:
        cnt+=1
print(cnt)